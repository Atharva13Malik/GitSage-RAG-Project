from app.rag_pipeline import index_repository, ask_gitsage


repo_url = input("Enter Github Repository URL: ")

result = index_repository(repo_url)

if not result["success"]:
    print(result["message"])
    exit()


print("\nRepository indexed successfully")
print("Files:", result["total_files"])
print("Documents:", result["total_documents"])
print("Chunks:", result["total_chunks"])


retriever = result["retriever"]


question = input("\nAsk a question about the repository: ")

explanation_style = input(
    "Choose explanation style (simple/concise/detailed/beginner-friendly): "
)


answer_result = ask_gitsage(
    question=question,
    explanation_style=explanation_style,
    retriever=retriever
)


if not answer_result["success"]:
    print(answer_result["message"])
    exit()


print("\nGitSage Answer:\n")
print(answer_result["answer"])


print("\nSources:")

for source in answer_result["sources"]:
    print("-", source)