from fastapi import FastAPI
from pydantic import BaseModel

from app.rag_pipeline import index_repository
from app.rag_pipeline import index_repository, ask_gitsage


app = FastAPI(
    title="GitSage API"
)


# Currently analyzed repository ka retriever backend memory me store hoga
current_retriever = None


# React/FastAPI request ka expected structure
class RepoRequest(BaseModel):
    repo_url: str

class AskRequest(BaseModel):
    question: str
    explanation_style: str


# Simple health-check endpoint
@app.get("/")
def home():
    return {
        "message": "GitSage API is running"
    }


# Repository analyze/index karne ka endpoint
@app.post("/analyze-repo")
def analyze_repo(request: RepoRequest):

    global current_retriever

    # Existing RAG pipeline call karo
    result = index_repository(request.repo_url)

    # Agar indexing fail hui
    if not result["success"]:
        return result

    # Retriever backend me store karo
    current_retriever = result["retriever"]

    # React ko clean JSON response bhejo
    return {
        "success": True,
        "message": result["message"],
        "repo_path": result["repo_path"],
        "total_files": result["total_files"],
        "total_documents": result["total_documents"],
        "total_chunks": result["total_chunks"]
    }

@app.post("/ask")
def ask_question(request: AskRequest):

    if current_retriever is None:
        return {
            "success": False,
            "message": "Please analyze a repository first."
        }

    result = ask_gitsage(
        question=request.question,
        explanation_style=request.explanation_style,
        retriever=current_retriever
    )

    return result