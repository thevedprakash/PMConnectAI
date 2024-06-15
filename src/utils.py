import math
from langchain_google_genai import GoogleGenerativeAIEmbeddings


import faiss
from langchain_community.vectorstores import FAISS
from langchain_community.docstore import InMemoryDocstore
from langchain.retrievers import TimeWeightedVectorStoreRetriever
from config import Config
import os

def relevance_score_fn(score: float) -> float:
    """
    Computes a relevance score for embedding vectors based on the provided score.
    
    Args:
        score (float): The initial score from the vector similarity measure.
    
    Returns:
        float: Adjusted relevance score.
    """
    """Calculate relevance score for vector embeddings."""
    return 1.0 - score / math.sqrt(2)

def create_new_memory_retriever():
    """
    Creates and configures a new memory retriever using Azure OpenAI embeddings with a FAISS vector store.
    
    Returns:
        TimeWeightedVectorStoreRetriever: Configured retriever ready for use with embedded data.
    """
    embeddings_model = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")
    embeddings_size =  768
    index = faiss.IndexFlatL2(embeddings_size)
    vectorstore = FAISS(embeddings_model, index, InMemoryDocstore({}), {}, relevance_score_fn=relevance_score_fn)
    return TimeWeightedVectorStoreRetriever(vectorstore=vectorstore, other_score_keys=["importance"], k=15) 