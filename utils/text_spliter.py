

from langchain_text_splitters import RecursiveCharacterTextSplitter as TextSplitter

from config import CHUNK_SIZE, CHUNK_OVERLAP

def split_text(text: str):


    text_spliter=TextSplitter(chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP)

    return text_spliter.split_documents(text)