from app.repo_loader import clone_repository
from app.document_loader import get_repository_files, load_documents
from app.chunker import create_chunks
from app.vector_store import create_vector_store
from app.retriever import create_retriever
from app.prompt import prompt
from app.llm import llm


def index_repository(repo_url):

    # 1. Repository clone karo
    repo_path = clone_repository(repo_url)

    if repo_path is None:
        return {
            "success": False,
            "message": "Failed to clone repository."
        }

    # 2. Useful files find karo
    files = get_repository_files(repo_path)

    if not files:
        return {
            "success": False,
            "message": "No supported files found in the repository."
        }

    # 3. Files ko LangChain Documents me convert karo
    documents = load_documents(files)

    # 4. Documents ko chunks me split karo
    chunks = create_chunks(documents)

    # 5. ChromaDB vector store create karo
    try:
        vector_store = create_vector_store(chunks)

    except Exception as error:
        return {
            "success": False,
            "message": f"Failed to create vector store: {error}"
        }

    # 6. Retriever create karo
    retriever = create_retriever(vector_store)

    # 7. Indexing information return karo
    return {
        "success": True,
        "message": "Repository indexed successfully.",
        "repo_path": str(repo_path),
        "total_files": len(files),
        "total_documents": len(documents),
        "total_chunks": len(chunks),
        "retriever": retriever
    }


def ask_gitsage(question, explanation_style, retriever):

    # 1. Relevant chunks retrieve karo
    try:
        retrieved_docs = retriever.invoke(question)

    except Exception as error:
        return {
            "success": False,
            "message": f"Failed to retrieve repository context: {error}"
        }

    if not retrieved_docs:
        return {
            "success": False,
            "message": "No relevant information was found in the repository."
        }

    # 2. Retrieved chunks se context banao
    context = ""

    for doc in retrieved_docs:
        context = context + "\n\n"
        context = context + "File: " + doc.metadata.get("file_path", "Unknown")
        context = context + "\n"
        context = context + doc.page_content

    # 3. Prompt format karo
    messages = prompt.format_messages(
        context=context,
        question=question,
        explanation_style=explanation_style
    )

    # 4. LLM se final answer generate karo
    try:
        response = llm.invoke(messages)

    except Exception as error:
        return {
            "success": False,
            "message": f"Failed to generate answer: {error}"
        }

    # 5. Unique source files nikalo
    sources = []

    for doc in retrieved_docs:
        file_path = doc.metadata.get("file_path")

        if file_path and file_path not in sources:
            sources.append(file_path)

    # 6. Final result return karo
    return {
        "success": True,
        "answer": response.content,
        "sources": sources
    }