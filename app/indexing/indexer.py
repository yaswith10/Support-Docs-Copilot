from pathlib import Path

from app.chunkers.base_chunker import BaseChunker
from app. embedders.base_embedder import BaseEmbedder
from app.loaders.base_loader import BaseLoader
from app.vectorstores.base_vector_store import BaseVectorStore

class Indexer:

    def __init__(
            self,
            loader: BaseLoader,
            chunker: BaseChunker,
            embedder: BaseEmbedder,
            vector_store: BaseVectorStore
        ):
        self.loader = loader
        self.chunker = chunker
        self.embedder = embedder
        self.vector_store = vector_store

    def index(self, directory: Path) -> None:
        documents = self.loader.load(directory)
        total_chunks = []
        for document in documents:
            chunks = self.chunker.chunk(document)
            total_chunks.extend(chunks)
        
        embeddings = self.embedder.embed(total_chunks)
        self.vector_store.add(total_chunks, embeddings)
    
            
    