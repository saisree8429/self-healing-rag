from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vectorstore = Chroma(
    persist_directory="chroma_db",
    embedding_function=embedding
)

retriever = vectorstore.as_retriever(
    search_type="mmr",
    search_kwargs={"k": 4}
)

def retrieve(state):
    question = state.get("rewritten_question") or state["question"]

    docs = retriever.invoke(question)

    return {
        "documents": [doc.page_content for doc in docs]
    }