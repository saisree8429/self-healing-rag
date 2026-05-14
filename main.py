from app.graph import graph

print("Self-Healing RAG Started!")
print("Type 'exit' to quit.\n")

while True:
    question = input("Ask Question: ")

    if question.lower() == "exit":
        break

    result = graph.invoke({
        "question": question,
        "rewritten_question": "",
        "documents": [],
        "answer": "",
        "critic_decision": "",
        "retries": 0
    })

    if result["critic_decision"] == "FAIL":
        print("\nI don't have enough information.\n")
    else:
        print("\nFinal Answer:\n")
        print(result["answer"])
        print()