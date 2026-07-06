from pathlib import Path

from app.chunkers.fixed_size_chunker import FixedSizeChunker
from app.embedders.sentence_transformer_embedder import SentenceTransformerEmbedder
from app.loaders.directory_loader import DirectoryLoader
from app.vectorstores.simple_vector_store import SimpleVectorStore

loader = DirectoryLoader()
chunker = FixedSizeChunker(20)
embedder = SentenceTransformerEmbedder()

documents = loader.load(Path("app/data/raw"))

chunks = []

for document in documents:
    chunks.extend(chunker.chunk(document))

embeddings = embedder.embed(chunks)

print(f"Chunks: {len(chunks)}")
print(f"Embeddings: {len(embeddings)}")
print(f"Embedding dimension: {len(embeddings[0])}")

vector_store = SimpleVectorStore()
vector_store.add(chunks=chunks, embeddings=embeddings)

query = embedder.embed_query("What is Fang Yuan Favorite Gu ?")

results = vector_store.search(query, k=3)

for result in results:
    print(result.score)
    print(result.chunk.text)
