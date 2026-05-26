from langchain_community.vectorstores import Chroma


def create_vector_store(documents,embeddig_model,collection_name="sample_collection"):


    vector_db=Chroma.from_documents(documents=documents, embedding=embeddig_model, collection_name=collection_name)
    return vector_db
