from langchain_google_genai import ChatGoogleGenerativeAI

from config import LLM_MODEL,GOOGLE_API_KEY


def load_llm():
    return ChatGoogleGenerativeAI(model=LLM_MODEL,temperature=0,google_api_key=GOOGLE_API_KEY)