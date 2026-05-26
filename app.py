
from loaders.txt_loader import load_documents
from utils.text_spliter import split_text

from embeddings.embedding_model import get_embedding_model

from vectorstore.chroma_store import create_vector_store

from llm.gemini_model import load_llm
from chains.rag_chain import create_rag_chain



#load document

documents=load_documents("data/jeevandas_CV.pdf")

#split document
chunks=split_text(documents)

#embedding model
embedding_model=get_embedding_model()

#create vector store
vector_store=create_vector_store(chunks,embedding_model)

retriver=vector_store.as_retriever()

#load llm
llm=load_llm()
#create rag chain
rag_chain=create_rag_chain(llm,retriver)

#query

while True:
    query=input("Enter your query: ")
    if query.lower() in ["exit","quit"]:
        print("Exiting the program.")
        break
    response=rag_chain.run(query)
    print(f"Answer: {response}\n")
