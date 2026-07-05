from pathlib import Path

from app.parsers.base_parser import BaseParser
from app.parsers.markdown_parser import MarkdownParser

class ParserFactory:

    _parsers = {
        ".md" : MarkdownParser()
    }

    @classmethod
    def get_parser(cls, file: Path) -> BaseParser | None:
        suffix = file.suffix.lower()
        return cls._parsers.get(file.suffix.lower())
    
