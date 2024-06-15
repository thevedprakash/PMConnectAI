import math
from langchain_google_genai import GoogleGenerativeAIEmbeddings


import faiss
from langchain_community.vectorstores import FAISS
from langchain_community.docstore import InMemoryDocstore
from langchain.retrievers import TimeWeightedVectorStoreRetriever
from config import Config
import os


def get_embedding_dimension(embeddings_model):
    # Generate a sample embedding
    sample_text = "This is a sample text to determine the embedding dimension."
    embedding = embeddings_model.embed_query(sample_text)
    return len(embedding)

# Initialize the embeddings model
embedding_model = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")

# Determine the embedding dimension
embedding_dimension = get_embedding_dimension(embedding_model)
print(f"Determined embedding dimension: {embedding_dimension}")
