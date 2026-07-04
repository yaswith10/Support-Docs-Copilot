from app.llm.groq_client import GroqLLM

class ChatEngine:
    def __init__(self, system_prompt):
        self.system_prompt = system_prompt
        self.llm = GroqLLM()

    def chat(self, prompt: str) -> str:
        return self.llm.generate(self.system_prompt ,prompt)
    