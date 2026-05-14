from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

GROQ_MODEL = "llama-3.1-8b-instant"

critic_llm = ChatGroq(
    model=GROQ_MODEL
)

def critic(state):
    context = "\n\n".join(state["documents"])
    answer = state["answer"]

    prompt = f"""
You are a strict hallucination detector.

Check whether the answer is fully supported by the context.

Reply ONLY with:
PASS
or
FAIL

Context:
{context}

Answer:
{answer}
"""

    response = critic_llm.invoke(prompt)

    decision = response.content.strip()

    return {
        "critic_decision": decision
    }