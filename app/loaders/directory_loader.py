from pathlib import Path

from app.models.document import Document
from app.loaders.base_loader import BaseLoader
from app.parsers.parser_factory import ParserFactory

class DirectoryLoader(BaseLoader):
    def load(self, directory: Path) -> list[Document]:
        documents = []

        for file in directory.rglob("*"):
            parser = ParserFactory.get_parser(file)
            document = parser.parse(file)
            documents.append(document)
        
        return documents