from app.loaders.directory_loader import DirectoryLoader
from pathlib import Path

loader = DirectoryLoader()
print(loader.load(Path("app/data/raw")))