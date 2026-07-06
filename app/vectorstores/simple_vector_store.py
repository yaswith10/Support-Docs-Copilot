import math

from app.models.chunk import Chunk
from app.models.search_result import SearchResult
from app.vectorstores.base_vector_store import  BaseVectorStore

class SimpleVectorStore(BaseVectorStore):
    
    def __init__(self):
        self._chunks: list[Chunk] = []
        self._embeddings: list[list[float]] = []

    def _cosine_similarity(self, vector1: list[float], vector2: list[float]) -> float:
        dot_product = sum(a * b for a,b in zip(vector1, vector2))
        norm1 = math.sqrt(sum(x * x for x in vector1))
        norm2 = math.sqrt(sum(x * x for x in vector2))

        if(norm1 == 0 or norm2 == 0):
            return 0.0
        
        return dot_product / (norm1 * norm2)

    def add(self, chunks: list[Chunk], embeddings: list[list[float]]) -> None:
        if(len(chunks) != len(embeddings)):
            raise ValueError(
                "Number of Chunks and Embeddings should match"
            )
        
        self._chunks.extend(chunks)
        self._embeddings.extend(embeddings)
        
    def search(self, query_embedding, k = 5) -> list[SearchResult]:
        results = []

        for chunk, embedding in zip(self._chunks, self._embeddings):
            score = self._cosine_similarity(query_embedding, embedding)

            results.append(
                SearchResult(chunk=chunk, score=score)
            )
        
        results.sort(key=lambda result: result.score, reverse=True)
        return results[:k]
    


    