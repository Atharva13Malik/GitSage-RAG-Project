from pathlib import Path

# Ab document_loader.py ko batana hai ki GitSage ko kaunsi files padhni hain.

SUPPORTED_EXTENSIONS={
  ".py",
  ".js",
  ".jsx",
  ".ts",
  ".tsx",
  ".java",
  ".md",
  ".json",
  ".html",
  ".css"
}

# Ab hum batayenge ki repository ke kaunse folders ko scan hi nahi karna.

IGNORED_FOLDERS = {
    ".git",
    "node_modules",
    ".venv",
    "dist",
    "build",
    "__pycache__",
}

useful_files=[]



def get_repository_files(repo_path):

    repo_path = Path(repo_path)

    useful_files = []

    for path in repo_path.rglob("*"):

        # 1. Sirf actual files chahiye
        if not path.is_file():
            continue

        # 2. Ignored folders ke andar ki files skip karo
        if any(folder in path.parts for folder in IGNORED_FOLDERS):
            continue

        # 3. Unsupported file extensions skip karo
        if path.suffix.lower() not in SUPPORTED_EXTENSIONS:
            continue

        # 4. Useful file ko list me add karo
        useful_files.append(path)

    # 5. Saari useful files return karo
    return useful_files
  