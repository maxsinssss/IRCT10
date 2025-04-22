import math
from collections import Counter

def preprocess(text):
    return text.lower().split()

def compute_cosine_similarity(query, document):
    
    query_words = preprocess(query)
    doc_words = preprocess(document)

    all_words = list(set(query_words + doc_words))

    query_vector = [query_words.count(word) for word in all_words]
    doc_vector = [doc_words.count(word) for word in all_words]

    dot_product = sum(q * d for q, d in zip(query_vector, doc_vector))
    norm_query = math.sqrt(sum(q ** 2 for q in query_vector))
    norm_doc = math.sqrt(sum(d ** 2 for d in doc_vector))

    if norm_query == 0 or norm_doc == 0:
        return 0.0
    else:
        return dot_product / (norm_query * norm_doc)

query = "gold silver truck"
document = "shipment of gold damaged in a gold fire"

similarity = compute_cosine_similarity(query, document)

print(f"Cosine Similarity: {similarity:.4f}")
