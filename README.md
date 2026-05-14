# self-healing-rag

A Python project that builds a self-healing Retrieval-Augmented Generation (RAG) pipeline using:

- **LangGraph** for stateful workflow orchestration
- **LangChain** integrations for document loading, text splitting, embeddings, and retrieval
- **Groq** as the chat language model provider
- **Chroma** for vector storage and semantic search

The application ingests a PDF, embeds its text, retrieves relevant passages for user questions, generates answers, and uses a critic step to detect unsupported responses. If the critique fails, the query is rewritten and retrieval is retried automatically.

## Features

- PDF ingestion and chunking
- Sentence-transformers embeddings with Chroma vector store
- LangGraph workflow with retrieve, generate, critic, and rewrite steps
- Automatic query rewriting on unsupported or hallucinated answers
- Interactive CLI for question answering

## Project Structure

- `main.py` - Entry point for the interactive assistant
- `app/graph.py` - Workflow definition using LangGraph
- `app/generate.py` - Answer generation with Groq chat model
- `app/retrieve.py` - Retrieval from Chroma vector store
- `app/critic.py` - Critic step to validate model answers
- `app/rewrite.py` - Query rewriting step when the critic fails
- `app/ingest.py` - PDF ingestion and embedding script
- `app/state.py` - Typed state definition for the workflow
- `requirements.txt` - Python dependencies
- `data/` - Source documents for ingestion
- `chroma_db/` - Persisted Chroma vector database

## Requirements

- Python 3.11+ or compatible environment
- Git (for repository operations)
- A valid Groq API key in `.env`

## Setup

```powershell
cd c:\Users\pabba\self-healing-rag
python -m pip install -r requirements.txt
```

Create a `.env` file with your Groq key:

```env
GROQ_API_KEY=your_groq_api_key_here
```

## Usage

Run the app:

```powershell
python main.py
```

Then ask questions in the prompt. Type `exit` to quit.

## Ingest new PDF

To re-ingest the document and refresh the Chroma database, run:

```powershell
python app\ingest.py
```

## Notes

- The current implementation uses a Groq model that must be available in your Groq account.
- The retrieval step uses `sentence-transformers/all-MiniLM-L6-v2` for embeddings.
- You may need a Hugging Face token if rate-limiting occurs.

## License

This repository is provided as-is.

