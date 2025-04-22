def preprocess(text):
    return text.lower().replace('.', '').split()

def build_inverted_index(docs):
    index = {}
    for doc_id, content in docs.items():
        words = preprocess(content)
        for word in words:
            if word not in index:
                index[word] = set()
            index[word].add(doc_id)
    return index

def boolean_and_query(index, query_terms):
    result = index.get(query_terms[0], set())
    for term in query_terms[1:]:
        result = result.intersection(index.get(term, set()))
    return result

def main():
    documents = {
        "Document 1": "The university exam is scheduled next week.",
        "Document 2": "The university of mumbai has declared the result."
    }

    inverted_index = build_inverted_index(documents)

    query = "university and mumbai"
    query_terms = [term.lower() for term in query.split() if term.lower() != "and"]

    result = boolean_and_query(inverted_index, query_terms)

    print("Query:", query)
    print("Documents matching the query:", result)

if __name__ == "__main__":
    main()
