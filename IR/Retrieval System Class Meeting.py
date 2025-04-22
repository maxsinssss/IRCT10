def preprocess(text):
    return text.lower().replace(".", "").split()

def build_inverted_index(documents):
    index = {}
    for doc_id, text in documents.items():
        words = preprocess(text)
        for word in words:
            if word not in index:
                index[word] = set()
            index[word].add(doc_id)
    return index

def retrieve_documents(index, query_terms):
    result_docs = set()
    for term in query_terms:
        if term in index:
            if not result_docs:
                result_docs = index[term]
            else:
                result_docs = result_docs.intersection(index[term])
        else:
            return set()  
    return result_docs

documents = {
        "Doc1": "The class will meet at 10 AM.",
        "Doc2": "The meeting has been rescheduled.",
        "Doc3": "We have a class meeting next Monday.",
        "Doc4": "This document is unrelated."
}

query = "class meeting"
query_terms = preprocess(query)

index = build_inverted_index(documents)
results = retrieve_documents(index, query_terms)

print(f"Query: {query}")
print("Documents containing all query terms:", results)


