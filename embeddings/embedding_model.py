from langchain_google_genai import GoogleGenerativeAIEmbeddings

from config import EMBEDDING_MODEL,GOOGLE_API_KEY

def get_embedding_model():
    """
    Initialize and return the embedding model.

    Returns:
        GoogleGenerativeAIEmbeddings: An instance of the embedding model.
    """
    return GoogleGenerativeAIEmbeddings(model=EMBEDDING_MODEL, google_api_key=GOOGLE_API_KEY)