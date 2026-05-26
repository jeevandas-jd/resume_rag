import os

from langchain_community.document_loaders import (
    TextLoader,
    PyPDFLoader
)

def load_documents(path):

    extension = os.path.splitext(path)[1]

    if extension == ".txt":

        loader = TextLoader(path)

    elif extension == ".pdf":

        loader = PyPDFLoader(path)

    else:
        raise ValueError(
            f"Unsupported file type: {extension}"
        )

    documents = loader.load()

    return documents