from transformers import pipeline
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain
import os, requests

def img2text(fp, mock = False):
    if mock: return "a group of pokemons"
    pipe = pipeline("image-to-text", model="Salesforce/blip-image-captioning-base")

    text = pipe(fp)[0]["generated_text"]
    return text

def tellAStory(openai_source, prompt, mock = False):
    if mock: return "I like bacon."
    if openai_source == "azure":
        print(f"USE AZURE AS SOURCE")
        from langchain_openai import AzureChatOpenAI
        # https://github.com/langchain-ai/langchain/issues/3137
        llm = AzureChatOpenAI(azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"), api_key=os.getenv("AZURE_OPENAI_API_KEY")
                        , azure_deployment=os.getenv("AZURE_OPENAI_CHATGPT_DEPLOYMENT"), model="gpt-35-turbo"
                        , api_version=os.getenv("OPENAI_API_VERSION"), openai_api_type="azure")
    else:
        print(f"USE OPENAI AS SOURCE")
        from langchain_openai import OpenAI
        llm = OpenAI(model="gpt-3.5-turbo-instruct")

    template = """You are a story teller; You can generate a short story based on a simple narrative,
    the story should be no more than 20 words; CONTEXT: {scenario} STORY:"""

    llm_prompt = PromptTemplate(input_variables=["scenario"],template=template,)

    chain = LLMChain(llm=llm, prompt=llm_prompt)

    return chain.run(prompt)

def query(payload, API_URL = "https://api-inference.huggingface.co/models/espnet/kan-bayashi_ljspeech_vits"):
	headers = {"Authorization": f'Bearer {os.getenv("HUGGINGFACE_API_TOKEN")}'}
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.content