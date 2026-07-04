from pathlib import Path
from app.models.document import Document
from app.parsers.base_parser import BaseParser

class MarkdownParser(BaseParser):
    def parse(self, file_path: str) -> Document:
        path = Path(file_path)
        text = path.read_text(encoding="utf-8")
        lines = text.splitlines()
        title = path.stem

        for line in lines:
            if line.startswith("# "):
                title = line[2:].strip()
                break

        return Document(
            id=path.stem,
            title=title,
            content=text,
            source=str(path),
            metadata={
                "extension" : path.suffix
            }
        )