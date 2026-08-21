def create_retriever(vector_store):

    retriever = vector_store.as_retriever(
        search_type="mmr",
        search_kwargs={
            #pehle 12 relevant candidates dekho ,unme k=4 final 4 diverse+relevant chunks add kro
            "k":4,
            "fetch_k":12
        }
    )

    return retriever