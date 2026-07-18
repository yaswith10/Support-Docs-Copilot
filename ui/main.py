import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

import streamlit as st

from app.vectorstores.simple_vector_store import SimpleVectorStore
from app.embedders.sentence_transformer_embedder import SentenceTransformerEmbedder
from app.indexing.indexer import Indexer
from app.loaders.directory_loader import DirectoryLoader
from app.chunkers.fixed_size_chunker import FixedSizeChunker
from app.retrieval.retriever import Retriever
from app.chat.chat_engine import ChatEngine
from app.prompts.prompt_builder import PromptBuilder
from app.llm.groq_client import GroqLLM


st.set_page_config(
    page_title="Support Docs Copilot",
    layout="wide"
)
# Necessary Functions
@st.cache_resource
def create_chat_engine():
    vector_store = SimpleVectorStore()

    embedder = SentenceTransformerEmbedder()

    indexer = Indexer(
        loader=DirectoryLoader(),
        chunker=FixedSizeChunker(),
        embedder=embedder,
        vector_store=vector_store,
    )

    indexer.index(Path("data/raw"))

    retriever = Retriever(
        embedder=embedder,
        vector_store=vector_store,
    )

    return ChatEngine(
        retriever=retriever,
        prompt_builder=PromptBuilder(),
        llm=GroqLLM(),
    )

# Sidebar
with st.sidebar:
    st.title("Support Docs Copilot")

    st.markdown("---")

    st.subheader("Status")

    if st.session_state.get("initialized", False):
        st.success("Documents Indexed")
    else:
        st.warning("Not Indexed")

    st.markdown("---")

    if st.button("🔄 Re-index Documents"):
        with st.spinner("Indexing..."):
            ...
        st.success("Indexing Complete!")

st.title("Support Docs Copilot")

# Session State

if "initialized" not in st.session_state:
    chat_engine = create_chat_engine()

    st.session_state.chat_engine = chat_engine
    st.session_state.intialized = True

    st.success("Documents Indexed Successfully !")

# Chat History

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat Input 

question = st.chat_input("Ask a question about your documentation...")

if question:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question,
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            answer = st.session_state.chat_engine.ask(question)

        st.markdown(answer)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer,
        }
    )