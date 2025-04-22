import math
from collections import defaultdict

def preprocess(text):
    return text.lower().replace(".", "").split()

def compute_tf(documents):
    tf = {}
    for doc_id, text in documents.items():
        tokens = preprocess(text)
        tf[doc_id] = defaultdict(int)
        for word in tokens:
            tf[doc_id][word] += 1
    return tf

def compute_idf(tf, N):
    idf = {}
    all_terms = set(term for doc in tf.values() for term in doc)
    for term in all_terms:
        df = sum(1 for doc in tf.values() if term in doc)
        idf[term] = math.log(N / (1 + df)) + 1  
    return idf

def compute_tfidf(tf, idf):
    tfidf = {}
    for doc_id, term_freqs in tf.items():
        tfidf[doc_id] = {}
        for term, freq in term_freqs.items():
            tfidf[doc_id][term] = freq * idf[term]
    return tfidf

def cosine_similarity(vec1, vec2):
    dot = sum(vec1.get(term, 0) * vec2.get(term, 0) for term in set(vec1) | set(vec2))
    norm1 = math.sqrt(sum(v**2 for v in vec1.values()))
    norm2 = math.sqrt(sum(v**2 for v in vec2.values()))
    if norm1 == 0 or norm2 == 0:
        return 0.0
    return dot / (norm1 * norm2)

def main():

    #Insert your data/documents
    documents = {
        "Doc1": "The sun is the star at the center of the solar system.",
        "Doc2": "She wore a beautiful dress to the party last night.",
        "Doc3": "The book on the table caught my attention immediately."
    }

    query = "solar system"
    preprocessed_query = preprocess(query)
    N = len(documents)

    tf_docs = compute_tf(documents)
    tf_query = {"Query": defaultdict(int)}
    for word in preprocessed_query:
        tf_query["Query"][word] += 1

    idf = compute_idf(tf_docs | tf_query, N)

    tfidf_docs = compute_tfidf(tf_docs, idf)
    tfidf_query = compute_tfidf(tf_query, idf)["Query"]

    print("Cosine Similarity with Query:", query)
    for doc_id, vec in tfidf_docs.items():
        score = cosine_similarity(tfidf_query, vec)
        print(f"{doc_id}: {score:.4f}")

if __name__ == "__main__":
    main()
