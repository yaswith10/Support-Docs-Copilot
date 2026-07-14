from pathlib import Path

from app.chunkers.fixed_size_chunker import FixedSizeChunker
from app.embedders.sentence_transformer_embedder import SentenceTransformerEmbedder
from app.indexing.indexing import Indexer
from app.loaders.directory_loader import DirectoryLoader
from app.vectorstores.simple_vector_store import SimpleVectorStore

vector_store = SimpleVectorStore()

indexer = Indexer(
    loader=DirectoryLoader(),
    chunker=FixedSizeChunker(),
    embedder=SentenceTransformerEmbedder(),
    vector_store=vector_store
)

indexer.index(Path("app/data/raw"))
print("Indexing Complete")