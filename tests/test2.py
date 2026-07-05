from pathlib import Path

from app.chunkers.fixed_size_chunker import FixedSizeChunker
from app.loaders.directory_loader import DirectoryLoader

loader = DirectoryLoader()

documents = loader.load(Path("app/data/raw"))
chunker = FixedSizeChunker(10)

for document in documents:
    chunks = chunker.chunk(document)
    print(document.title)
    print(f"Chunks: {len(chunks)}")

    for chunk in chunks:
        print(chunk.text)

