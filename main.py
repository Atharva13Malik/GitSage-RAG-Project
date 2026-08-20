from app.repo_loader import clone_repository

repo_url=input("Enter Github Repository URL: ")

repo_path=clone_repository(repo_url)

print("Repository location:", repo_path)