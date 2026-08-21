from app.repo_loader import clone_repository
from app.document_loader import get_repository_files, load_documents
from app.chunker import create_chunks
from app.vector_store import create_vector_store
from app.retriever import create_retriever
from app.llm import llm
from app.prompt import prompt


# 1. GET GITHUB REPOSITORY URL
repo_url = input("Enter Github Repository URL: ")


# 2. CLONE REPOSITORY
repo_path = clone_repository(repo_url)

if repo_path is None:
    print("Please check the GitHub repository URL.")
    exit()

print("\nRepository location:", repo_path)


# 3. FIND USEFUL FILES
files = get_repository_files(repo_path)

if not files:
    print("\nNo supported files found in the repository.")
    exit()

print("\nUseful files found:")

for file in files:
    print(file)


# 4. CONVERT FILES INTO LANGCHAIN DOCUMENTS
documents = load_documents(files)

print("\nTotal documents:", len(documents))

if documents:
    print("\nFirst document metadata:")
    print(documents[0].metadata)

    print("\nFirst document content preview:")
    print(documents[0].page_content[:300])


# 5. SPLIT DOCUMENTS INTO CHUNKS
chunks = create_chunks(documents)

print("\nTotal chunks:", len(chunks))


# 6. CREATE CHROMADB VECTOR STORE
try:
    vector_store = create_vector_store(chunks)

    print("\nChromaDB created successfully")

    stored_count = vector_store._collection.count()
    print("Chunks stored in ChromaDB:", stored_count)

except Exception as error:
    print("\nFailed to create vector store.")
    print("Reason:", error)
    exit()


# 7. CREATE MMR RETRIEVER
retriever = create_retriever(vector_store)


# 8. ASK QUESTION ABOUT REPOSITORY
question = input("\nAsk a question about the repository: ")


# 9. RETRIEVE RELEVANT CHUNKS
retrieved_docs = retriever.invoke(question)

if not retrieved_docs:
    print("\nGitSage Answer:")
    print("No relevant information was found in the repository.")
    exit()


# 10. BUILD CONTEXT FOR THE PROMPT
context = ""

for doc in retrieved_docs:
    context = context + "\n\n"
    context = context + "File: " + doc.metadata.get("file_path", "Unknown")
    context = context + "\n"
    context = context + doc.page_content


# 11. GET EXPLANATION STYLE
explanation_style = input(
    "\nChoose explanation style (simple/concise/detailed/beginner-friendly): "
)


# 12. FORMAT PROMPT
messages = prompt.format_messages(
    context=context,
    question=question,
    explanation_style=explanation_style
)


# 13. GENERATE FINAL ANSWER
try:
    response = llm.invoke(messages)

    print("\nGitSage Answer:\n")
    print(response.content)

except Exception as error:
    print("\nFailed to generate answer from LLM.")
    print("Reason:", error)
    exit()


# 14. SHOW UNIQUE SOURCE FILES
sources = []

for doc in retrieved_docs:
    file_path = doc.metadata.get("file_path")

    if file_path not in sources:
        sources.append(file_path)


print("\nSources:")

for source in sources:
    print("-", source)