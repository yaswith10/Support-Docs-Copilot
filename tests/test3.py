from pathlib import Path

from app.chunkers.fixed_size_chunker import FixedSizeChunker
from app.embedders.sentence_transformer_embedder import SentenceTransformerEmbedder
from app.loaders.directory_loader import DirectoryLoader

loader = DirectoryLoader()
chunker = FixedSizeChunker(10)
embedder = SentenceTransformerEmbedder()

documents = loader.load(Path("app/data/raw"))

chunks = []

for document in documents:
    chunks.extend(chunker.chunk(document))

embedding = embedder.embed(chunks)

print(f"Chunks: {len(chunks)}")
print(f"Embeddings: {len(embedding)}")
print(f"Embedding dimension: {len(embedding[0])}")