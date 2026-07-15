# from app.llm.groq_client import GroqLLM
from app.llm.base import BaseLLM
from app.prompts.prompt_builder import PromptBuilder
from app.retrieval.retriever import Retriever

class ChatEngine:
    def __init__(self, retriever: Retriever, prompt_builder: PromptBuilder, llm: BaseLLM):
        self.retriever: Retriever = retriever
        self.prompt_builder: PromptBuilder = prompt_builder
        self.llm: BaseLLM = llm
    
    def ask(self, question: str, k: int = 5):
        search_results = self.retriever.retrieve(question, k)
        prompt = self.prompt_builder.build(question, search_results)
        answer = self.llm.generate(prompt)
        return answer
    