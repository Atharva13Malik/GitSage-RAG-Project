import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")

llm = ChatGroq(
    model="openai/gpt-oss-120b",
    api_key=groq_api_key,
    temperature=0  #kafi close answer aaye
)

def test_llm():

    response = llm.invoke("Explain what Git is in one line.")

    print(response.content)
