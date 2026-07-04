from pathlib import Path

from app.models.document import Document
from app.loaders.base_loader import BaseLoader
from app.parsers.markdown_parser import MarkdownParser

class DirectoryLoader(BaseLoader):
    def load(self, directory: Path) -> list[Document]:
        documents = []
        parser = MarkdownParser()
        for file in directory.rglob("*.md"):
            document = parser.parse(file)
            documents.append(document)
        
        return documents