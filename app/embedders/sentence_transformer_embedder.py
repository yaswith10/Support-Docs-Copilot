from sentence_transformers import SentenceTransformer

from app.embedders.base_embedder import BaseEmbedder
from app.models.chunk import Chunk


class SentenceTransformerEmbedder(BaseEmbedder):

    def __init__(self, model_name="all-MiniLM-L6-v2"):
        self.model: SentenceTransformer = SentenceTransformer(model_name)
    

    def embed(self, chunks: list[Chunk]) -> list[list[float]]:
        # Currently we are use list[list[float]] after we will change it to list[EmbeddedChunk]
        texts = [chunk.text for chunk in chunks]

        embeddings = self.model.encode(
            texts,
            convert_to_numpy=True,
            show_progress_bar=False
        )

        return embeddings.tolist()
    
    def embed_query(self, query: str) -> list[list[float]]:
        embeddings = self.model.encode(
            query,
            convert_to_numpy=True,
            show_progress_bar=False
        )

        return embeddings.tolist()