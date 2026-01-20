from langchain.chains import RetrievalQA
from langchain.llms import OpenAI

def build_qa_chain(retriever):
    llm = OpenAI(temperature=0)
    qa = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff"
    )
    return qa
