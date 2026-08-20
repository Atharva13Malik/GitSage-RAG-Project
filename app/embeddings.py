import os

from dotenv import load_dotenv
from huggingface_hub import InferenceClient
from langchain_huggingface import HuggingFaceEmbeddings

load_dotenv()

hf_token = os.getenv("HF_TOKEN")

client=InferenceClient(
  token=hf_token
)
EMBEDDING_MODEL = "sentence-transformers/all-mpnet-base-v2"

def test_embedding():

    text = "GitSage helps understand GitHub repositories."

    embedding = client.feature_extraction(
        text,
        model=EMBEDDING_MODEL
    )

    print("Embedding generated successfully")
    print("Vector length:", len(embedding))
