from flipkart.config import Config
from langchain_groq import ChatGroq

print("Model:", Config.RAG_MODEL)
print("Key loaded:", bool(Config.GROQ_API_KEY))

llm = ChatGroq(model=Config.RAG_MODEL, api_key=Config.GROQ_API_KEY)
print(llm.invoke("Say hi").content)