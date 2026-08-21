from langchain_chroma import Chroma
from app.embeddings import HuggingFaceAPIEmbeddings

embedding_function=HuggingFaceAPIEmbeddings()


# main.py se chunks hmare isi function meh aayenge aur vector bnenge aur store honge
def create_vector_store(chunks):
      vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_function,
        collection_name="gitsage",
        persist_directory="vector_store"
    )
      return vector_store