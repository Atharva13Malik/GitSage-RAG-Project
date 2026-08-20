from langchain_text_splitters import RecursiveCharacterTextSplitter


def create_chunks(documents):

    # Text splitter configure karna
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=150
    )

    # Documents ko smaller chunks me split karna
    chunks = text_splitter.split_documents(documents)

    # Saare chunks return karna
    return chunks