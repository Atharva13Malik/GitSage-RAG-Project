# STEP 1: Import function for cloning GitHub repository
from app.repo_loader import clone_repository

# STEP 2: Import functions for finding useful files
# and converting them into LangChain Documents
from app.document_loader import get_repository_files, load_documents

# STEP 3: Import function for splitting Documents into chunks
from app.chunker import create_chunks

# STEP 4: Import function for generating embeddings
from app.embeddings import generate_embeddings


# 1. GET GITHUB REPOSITORY URL

repo_url = input("Enter Github Repository URL: ")


# 2. CLONE REPOSITORY

repo_path = clone_repository(repo_url)

print("\nRepository location:", repo_path)


# 3. FIND USEFUL FILES

files = get_repository_files(repo_path)

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

if chunks:
    print("\nFirst chunk metadata:")
    print(chunks[0].metadata)

    print("\nFirst chunk content preview:")
    print(chunks[0].page_content[:500])


# 6. GENERATE EMBEDDINGS

embeddings = generate_embeddings(chunks)

print("\nTotal embeddings:", len(embeddings))

if len(embeddings) > 0:
    print("First embedding vector length:", len(embeddings[0]))