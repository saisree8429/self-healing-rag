from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

GROQ_MODEL = "llama-3.1-8b-instant"

llm = ChatGroq(
    model=GROQ_MODEL
)

def rewrite(state):
    question = state["question"]

    prompt = f"""
Rewrite this question to improve retrieval.

Question:
{question}
"""

    response = llm.invoke(prompt)

    return {
        "rewritten_question": response.content,
        "retries": state["retries"] + 1
    }