import os

from dotenv import load_dotenv
from huggingface_hub import InferenceClient
from langchain_huggingface import HuggingFaceEmbeddings


# .env file load karna
load_dotenv()


# Hugging Face API client banana
hf_token = os.getenv("HF_TOKEN")

client=InferenceClient(
  token=hf_token
)


# Hugging Face API client banana
EMBEDDING_MODEL = "sentence-transformers/all-mpnet-base-v2"


# Simple test function

def test_embedding():

    text = "GitSage helps understand GitHub repositories."

    embedding = client.feature_extraction(
        text,
        model=EMBEDDING_MODEL
    )

    print("Embedding generated successfully")
    print("Vector length:", len(embedding))

# Actual project chunks ke text nikalna
def generate_embeddings(chunks):

    texts = []

    for chunk in chunks:
        texts.append(chunk.page_content)

    embeddings=client.feature_extraction(
        texts,
        model=EMBEDDING_MODEL
    )

    return embeddings

