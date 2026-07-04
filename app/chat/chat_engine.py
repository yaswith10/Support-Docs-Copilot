from app.llm.groq_client import GroqLLM

class ChatEngine:
    def __init__(self):
        self.llm = GroqLLM()

    def chat(self, prompt: str) -> str:
        return self.llm.generate(prompt)
    
    