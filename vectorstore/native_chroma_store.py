import chromadb

from chromadb.config import Settings

def create_chroma_client():

    client=chromadb.Client(Settings(
        persist_directory="./chroma_db"))
    
    return client


def create_chroma_collection(client, collection_name):
    collection = client.get_or_create_collection(name=collection_name)
    return collection
def add_to_chroma_collection(collection, documents, metadatas, ids):
    collection.add(
        documents=documents,
        metadatas=metadatas,
        ids=ids
    )   
def query_chroma_collection(collection, query, n_results=5):
    results = collection.query(
        query_texts=[query],
        n_results=n_results
    )
    return results

