from app.chunkers.base_chunker import BaseChunker
from app.models.document import Document
from app.models.chunk import Chunk

class FixedSizeChunker(BaseChunker):
    def __init__(self, chunk_size = 500):
        self.chunk_size = chunk_size

    def chunk(self, document: Document) -> list[Chunk]:
        chunks = []

        text = " ".join(document.content.split())

        for index, start in enumerate(range(0, len(text), self.chunk_size)):
            end = start + self.chunk_size
            chunk = Chunk(
                id=f"{document.id}_{index}",
                document_id=document.id,
                text=text[start: end],
                chunk_index=index
            )

            chunks.append(chunk)
        
        return chunks
    
