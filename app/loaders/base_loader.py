from abc import ABC, abstractmethod
from pathlib import Path
from app.models.document import Document

class BaseLoader(ABC):

    @abstractmethod
    def load(self, directory: Path) -> list[Document]:
        pass