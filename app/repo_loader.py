# User GitHub repo URL dega, aur GitSage us repository ko local repos/ folder me clone karega.

from git import Repo
from pathlib import Path


def clone_repository(repo_url):
    repo_name = repo_url.rstrip("/").split("/")[-1]

    repo_path = Path("repos") / repo_name

    if repo_path.exists():
        print(f"Repository already exists: {repo_path}")
        return repo_path

    print("Cloning repository...")

    Repo.clone_from(repo_url, repo_path)

    print(f"Repository cloned successfully: {repo_path}")

    return repo_path