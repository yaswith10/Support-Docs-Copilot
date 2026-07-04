from .base import BaseLLM
from groq import Groq
import os
from dotenv import load_dotenv
load_dotenv()

class GroqLLM(BaseLLM):

    def __init__(self):
        self.client = Groq(
            api_key = os.environ.get("GROQ_API_KEY")
        )

    def generate(self, system_prompt, prompt):
        client = self.client
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role" : "system",
                    "content" : system_prompt
                },
                {
                    "role" : "user",
                    "content" : prompt
                }
            ]
        )

        return response.choices[0].message.content