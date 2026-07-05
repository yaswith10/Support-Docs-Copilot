from abc import ABC, abstractmethod

from app.models.document import Document
from app.models.chunk import Chunk

class BaseChunker(ABC):
    @abstractmethod
    def chunk(self, document: Document) -> list[Chunk]:
        pass