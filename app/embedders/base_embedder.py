from abc import ABC, abstractmethod

from app.models.chunk import Chunk

class BaseEmbedder(ABC):

    @abstractmethod
    def embed(self, chunks: list[Chunk]) -> list[list[float]]:
        """
        Generate embeddings for a list of chunks
        """
        pass