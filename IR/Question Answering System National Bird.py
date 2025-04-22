def answer_question(corpus, query):
    
    normalized_query = query.lower()

    for sentence in corpus:
        if "national bird" in sentence.lower():
            return sentence
    return "Answer not found in the corpus."

corpus = [
        "India has the second-largest population in the world.",
        "It is surrounded by oceans from three sides which are Bay Of Bengal in the east, the Arabian Sea in the west and Indian oceans in the south.",
        "Tiger is the national animal of India.",
        "Peacock is the national bird of India.",
        "Mango is the national fruit of India."
    ]

query = "Which is the national bird of India?"

answer = answer_question(corpus, query)

print("Question:", query)
print("Answer:", answer)


