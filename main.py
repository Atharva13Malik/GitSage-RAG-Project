from app.repo_loader import clone_repository
from app.document_loader import get_repository_files

repo_url=input("Enter Github Repository URL: ")

repo_path=clone_repository(repo_url)

print("Repository location:", repo_path)

get_repository_files(repo_path)

files = get_repository_files(repo_path)

print("\nUseful files found:")

for file in files:
    print(file)