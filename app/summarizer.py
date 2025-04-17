import os
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv

load_dotenv()

def summarize_text(input_text: str) -> str:
    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
    template = "Summarize the following text:\n\n{text}"
    prompt = PromptTemplate(input_variables=["text"], template=template)
    chain = LLMChain(llm=llm, prompt=prompt)
    return chain.run(input_text)
