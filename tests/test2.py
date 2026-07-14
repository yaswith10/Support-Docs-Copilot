from pathlib import Path

from app.chunkers.fixed_size_chunker import FixedSizeChunker
from app.embedders.sentence_transformer_embedder import SentenceTransformerEmbedder
from app.indexing.indexer import Indexer
from app.loaders.directory_loader import DirectoryLoader
from app.retrieval.retriever import Retriever
from app.vectorstores.simple_vector_store import SimpleVectorStore


def main():

    # Create components
    loader = DirectoryLoader()
    chunker = FixedSizeChunker(chunk_size=500)
    embedder = SentenceTransformerEmbedder()
    vector_store = SimpleVectorStore()

    # Index documents
    indexer = Indexer(
        loader=loader,
        chunker=chunker,
        embedder=embedder,
        vector_store=vector_store,
    )

    indexer.index(Path("app/data/raw"))

    print("✅ Documents indexed successfully!\n")

    print(f"Chunks stored: {len(vector_store._chunks)}")
    print(f"Embeddings stored: {len(vector_store._embeddings)}")

    # Create retriever
    retriever = Retriever(
        embedder=embedder,
        vector_store=vector_store,
    )

    # Query
    query = "Who invented the Helios-7 Reactor?"

    print(f"Query: {query}\n")

    results = retriever.retrieve(query, k=3)

    for i, result in enumerate(results, start=1):
        print("=" * 80)
        print(f"Result {i}")
        print(f"Similarity Score: {result.score:.4f}")
        print(f"Chunk ID: {result.chunk.id}")
        print(f"Document ID: {result.chunk.document_id}")
        print()
        print(result.chunk.text)
        print()


if __name__ == "__main__":
    main()