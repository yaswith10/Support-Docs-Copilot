from app.embedders.base_embedder import BaseEmbedder
from app.vectorstores.base_vector_store import BaseVectorStore

class Retriever:
    def __init__(self, embedder: BaseEmbedder, vector_store: BaseVectorStore):
        self.embedder = embedder
        self.vector_store = vector_store
    
    def retrieve(self, query: str, k: int = 5):
        query_embedding = self.embedder.embed_query(query)

        return self.vector_store.search(query_embedding,k)
    
        