# self-healing-rag
A small Python project that builds a self-healing RAG pipeline using LangGraph, LangChain, Groq, and Chroma. It ingests a PDF, embeds its content, retrieves relevant passages, generates answers with a Groq chat model, and automatically rewrites queries when the critic detects unsupported responses.
