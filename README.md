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

# RAG-Based Document Question Answering System

## Overview
This project implements a Retrieval-Augmented Generation (RAG) pipeline
to answer user questions from PDF documents using semantic search and LLMs.

## Architecture
PDF → Chunking → Embeddings → FAISS → Retriever → LLM → Answer

## Tech Stack
Python, LangChain, FAISS, SentenceTransformers, OpenAI

## How to Run
1. Install dependencies: pip install -r requirements.txt
2. Add PDFs to data/sample_docs/
3. Run: python app.py

## Example Questions
- What is Retrieval-Augmented Generation?
- Explain vector embeddings
- What is NLP?

## Key Learnings
- Reduced hallucinations using retrieval grounding
- Modular GenAI system design
