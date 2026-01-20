# RAG-Based Document Question Answering System

This project implements a Retrieval-Augmented Generation (RAG) pipeline
to answer user queries from uploaded documents.

## Features
- PDF document ingestion
- Text chunking for context preservation
- Semantic embeddings using Sentence Transformers
- Vector similarity search using FAISS
- LLM-based answer generation grounded in document context
- Reduced hallucinations through retrieval grounding

## Architecture
Document → Chunking → Embeddings → Vector Store → Retriever → LLM → Answer

## Tech Stack
Python, LangChain, FAISS, HuggingFace, OpenAI

