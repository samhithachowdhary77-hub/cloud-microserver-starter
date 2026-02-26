from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from app.rag.retriever import get_retriever

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

prompt = ChatPromptTemplate.from_template(
"""
You are a DevOps troubleshooting assistant.

Use ONLY the provided runbook context to answer.

Context:
{context}

Question:
{question}
"""
)

def ask_agent(question: str):

    retriever = get_retriever()
    docs = retriever.invoke(question)

    context = "\n".join([d.page_content for d in docs])

    chain = prompt | llm

    response = chain.invoke({
        "context": context,
        "question": question
    })

    return response.content