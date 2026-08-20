# STEP 1: Import function for cloning GitHub repository
from app.repo_loader import clone_repository

# STEP 2: Import function for finding useful/supported files from repository
from app.document_loader import get_repository_files

from app.document_loader import get_repository_files, load_documents


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

print("\nTotal documents:", len(documents))

if documents:
    print("\nFirst document metadata:")
    print(documents[0].metadata)

    print("\nFirst document content preview:")
    print(documents[0].page_content[:300])


