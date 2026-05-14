from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

GROQ_MODEL = "llama-3.1-8b-instant"

llm = ChatGroq(
    model=GROQ_MODEL
)

def generate(state):
    context = "\n\n".join(state["documents"])
    question = state["question"]

    prompt = f"""
You are a helpful AI assistant.

Answer ONLY from the provided context.

Context:
{context}

Question:
{question}
"""

    response = llm.invoke(prompt)

    return {
        "answer": response.content
    }