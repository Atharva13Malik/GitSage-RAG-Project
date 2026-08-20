from pathlib import Path
from langchain_core.documents import Document

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



# Useful files ke andar ka actual code/text read karna
def load_documents(files):

    documents = []

    for file_path in files:

        # File ke andar ka complete text/code read karo
        content = file_path.read_text(encoding="utf-8")

        #File ke andar ke readed code ko LangChain Document banana
        document = Document(
         page_content=content,
         metadata={
         "file_name": file_path.name,
         "file_path": str(file_path),
         "file_type": file_path.suffix
         }
        )

         # Document ko list me add karo
        documents.append(document)

    # Saare documents return karo
    return documents
        



