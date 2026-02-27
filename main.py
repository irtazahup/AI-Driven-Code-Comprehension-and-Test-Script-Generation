from fastapi import FastAPI
from pydantic import BaseModel
from langchain_community.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
import pickle

app = FastAPI()

# 1. Load embeddings model (same as Colab)
with open("embedding_model.pkl", "rb") as f:
    embedding_model = pickle.load(f)

# 2. Load FAISS index (local folder)
vectorstore = FAISS.load_local("faiss_index", embedding_model, allow_dangerous_deserialization=True)

# 3. Create retriever
retriever = vectorstore.as_retriever()

class QueryRequest(BaseModel):
    query: str

@app.post("/ask")
async def ask_question(request: QueryRequest):
    docs = retriever.invoke(request.query)
    if not docs:
        return {"answer": "No relevant context found"}
    
    return {"answer": docs[0].page_content}
