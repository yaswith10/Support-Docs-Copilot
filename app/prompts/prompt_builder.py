from pathlib import Path

from app.models.search_result import SearchResult

class PromptBuilder:

    def __init__(self):
        prompt_path = Path("app/prompts/system_prompt.txt")
        self.system_prompt = prompt_path.read_text(encoding="utf-8")

    def build(self, question: str, search_results: list[SearchResult]) -> str:
        context = "\n\n".join(result.chunk.text for result in search_results)
        return f"""
{self.system_prompt}

------------------------------------------------
Context:
{context}

------------------------------------------------

Question:
{question}

Answer:"""
