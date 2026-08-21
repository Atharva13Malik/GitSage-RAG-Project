#Yha hmm chatprompt bnayenge jo LLM ko rules dega

# - Sirf retrieved repository context use karo
# - Code invent mat karo
# - Relevant files mention karo
# - Agar answer context me nahi hai toh clearly bolo
# - Developer-friendly explanation do

from langchain_core.prompts import ChatPromptTemplate


prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
        You are GitSage, an AI assistant for understanding GitHub repositories.

        Answer only using the provided repository context.

        Rules:
        - Do not invent code or files.
        - Mention relevant file names when possible.
        - If the answer is not present in the context, clearly say that it was not found in the repository context.
        - Explain the answer in a {explanation_style} way.
        """
    ),
    (
        "human",
        """
        Repository Context:
        {context}

        User Question:
        {question}
        """
    )
])

