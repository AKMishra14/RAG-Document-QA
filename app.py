from src.loader import load_documents
from src.chunker import chunk_documents
from src.embedder import create_vector_store
from src.retriever import load_retriever
from src.qa_chain import build_qa_chain

# Step 1: Load & index document
docs = load_documents("data/sample_docs/ai_notes.pdf")
chunks = chunk_documents(docs)
create_vector_store(chunks)

# Step 2: Ask questions
retriever = load_retriever()
qa = build_qa_chain(retriever)

while True:
    question = input("Ask a question: ")
    print(qa.run(question))

