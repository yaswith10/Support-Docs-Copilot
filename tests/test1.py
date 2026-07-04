from app.llm.groq_client import GroqLLM

def main():
    llm = GroqLLM()
    response = llm.generate("Who is PM of India")
    print(response)

if __name__ == "__main__":
    main()