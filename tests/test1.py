from pathlib import Path

from app.chunkers.fixed_size_chunker import FixedSizeChunker
from app.embedders.sentence_transformer_embedder import SentenceTransformerEmbedder
from app.indexing.indexer import Indexer
from app.llm.groq_client import GroqLLM
from app.loaders.directory_loader import DirectoryLoader
from app.prompts.prompt_builder import PromptBuilder
from app.retrieval.retriever import Retriever
from app.chat.chat_engine import ChatEngine
from app.vectorstores.simple_vector_store import SimpleVectorStore


vector_store = SimpleVectorStore()

embedder = SentenceTransformerEmbedder()

indexer = Indexer(
    loader=DirectoryLoader(),
    chunker=FixedSizeChunker(),
    embedder=embedder,
    vector_store=vector_store,
)

indexer.index(Path("app/data/raw"))

retriever = Retriever(
    embedder=embedder,
    vector_store=vector_store,
)

chat_engine = ChatEngine(
    retriever=retriever,
    prompt_builder=PromptBuilder(),
    llm=GroqLLM(),
)

while True:
    question = input("\nAsk a question (type 'exit' to quit): ")

    if question.lower() == "exit":
        break

    answer = chat_engine.ask(question)

    print("\nAnswer:")
    print(answer)