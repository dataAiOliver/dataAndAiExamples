# https://learn.microsoft.com/en-us/samples/azure-samples/function-python-ai-langchain/function-python-ai-langchain/
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain
import os

load_dotenv()

AZURE_OPENAI_CHATGPT_DEPLOYMENT = os.getenv("AZURE_OPENAI_CHATGPT_DEPLOYMENT")
print(f"AZURE_OPENAI_CHATGPT_DEPLOYMENT: {AZURE_OPENAI_CHATGPT_DEPLOYMENT}")
AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
print(f"AZURE_OPENAI_API_KEY: {AZURE_OPENAI_API_KEY}")
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
print(f"AZURE_OPENAI_ENDPOINT: {AZURE_OPENAI_ENDPOINT}")
OPENAI_API_VERSION = os.getenv("OPENAI_API_VERSION")
print(f"OPENAI_API_VERSION: {OPENAI_API_VERSION}")

def tellAStory(openai_source, prompt):

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

prompt = "A dog and a cat."
openai_source = "azure"
story = tellAStory(openai_source, prompt)
print(f"The story: '{story}'")