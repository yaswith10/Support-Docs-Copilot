from abc import ABC, abstractmethod

from app.models.chunk import Chunk
from app.models.search_result import SearchResult

class BaseVectorStore(ABC):

    @abstractmethod
    def add(self, chunks: list[Chunk], embeddings: list[list[float]]) -> None:
        pass

    @abstractmethod
    def search(self, query_embedding: list[float], k: int = 5) -> list[SearchResult]:
        pass

