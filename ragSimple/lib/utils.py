from langchain.chains import RetrievalQA
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.llms import LlamaCpp
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.document_loaders import PyPDFDirectoryLoader
import os
from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI

load_dotenv()

def get_llm(openai_source):
    # get llm
    if openai_source == "azure":
        print(f"USE AZURE AS SOURCE")
        from langchain_openai import AzureChatOpenAI
        # https://github.com/langchain-ai/langchain/issues/3137
        llm = AzureChatOpenAI(azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"), api_key=os.getenv("AZURE_OPENAI_API_KEY")
                        , azure_deployment=os.getenv("AZURE_OPENAI_CHATGPT_DEPLOYMENT"), model="gpt-35-turbo"
                        , api_version=os.getenv("OPENAI_API_VERSION"), openai_api_type="azure")
    elif openai_source == "openai":
        print(f"USE OPENAI AS SOURCE")
        from langchain_openai import OpenAI
        llm = OpenAI(model="gpt-3.5-turbo-instruct")
    else:
        print("Error: Provide Proper LLM-Source.")
        return None
    
    return llm
    
def get_vector_store(fp_pdfs):
    print(f"START: GET VECTOR STORE")

    # read pdfs
    data_pdfs = PyPDFDirectoryLoader(fp_pdfs).load()

    # split in chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=20)
    text_chunks = text_splitter.split_documents(data_pdfs)

    # embedding
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    # vectors for storing
    return FAISS.from_documents(text_chunks, embedding=embeddings)

def get_qa(fp_pdfs, openai_source):
    print(f"START: GET QA")
    llm = get_llm(openai_source)
    vector_store = get_vector_store(fp_pdfs)
    return RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=vector_store.as_retriever(search_kwargs={"k": 2}))
