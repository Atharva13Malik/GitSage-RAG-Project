# STEP 1: Import function for cloning GitHub repository
from app.repo_loader import clone_repository

# STEP 2: Import function for finding useful/supported files from repository
from app.document_loader import get_repository_files

from app.document_loader import get_repository_files, load_documents

from app.chunker import create_chunks


# STEP 3: Take GitHub repository URL from user
repo_url = input("Enter Github Repository URL: ")


# STEP 4: Clone the repository inside the repos/ folder
# If repository already exists, it will use the existing repository
repo_path = clone_repository(repo_url)


# STEP 5: Display the local path where repository is stored
print("Repository location:", repo_path)


# STEP 6: Get only useful files from the repository
# Example: .py, .js, .java, .md, .json etc.
# Ignored folders like .git, node_modules, .venv etc. are skipped
files = get_repository_files(repo_path)

documents = load_documents(files)
chunks=create_chunks(documents)

print("\nTotal documents:", len(documents))
print("Total chunks:", len(chunks))

if chunks:
    print("\nFirst chunk metadata:")
    print(chunks[0].metadata)

    print("\nFirst chunk content:")
    print(chunks[0].page_content[:500])


