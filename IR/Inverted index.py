def preprocess(text):
    return text.lower().replace(".", "").split()

def build_inverted_index(docs):
    inverted_index = {}
    for doc_id, text in docs.items():
        words = preprocess(text)
        for word in words:
            if word not in inverted_index:
                inverted_index[word] = set()
            inverted_index[word].add(doc_id)
    return inverted_index


documents = {
        "Doc1": "our class meeting starts soon",
        "Doc2": "my class starts at 6."
}


index = build_inverted_index(documents)

print("Inverted Index:")
for term, doc_ids in index.items():
        print(f"{term}: {sorted(doc_ids)}")

