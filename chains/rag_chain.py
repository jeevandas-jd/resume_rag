from langchain_classic.chains import RetrievalQA


def create_rag_chain(llm,retriever):
    """
    Create a RetrievalQA chain using the provided language model and retriever.

    Args:
        llm: The language model to use for generating answers.
        retriever: The retriever to use for fetching relevant documents."""
    return RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
