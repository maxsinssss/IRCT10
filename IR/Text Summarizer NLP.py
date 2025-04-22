from collections import Counter
import re

def preprocess_text(text):
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    text = text.lower()
    return text

def get_most_frequent_words(text, num_words=5):
    words = text.split()
    frequency = Counter(words)
    most_common = frequency.most_common(num_words)
    keywords = [word for word, freq in most_common]
    return keywords

def summarize_text(text, keywords):
    
    sentences = text.split('.')
    summary = []
    for sentence in sentences:
        if any(keyword in sentence.lower() for keyword in keywords):
            summary.append(sentence.strip())
    return ' '.join(summary)

text = """Natural language processing (NLP) is a field of computer science, artificial intelligence, and computational linguistics concerned with the interactions between computers and human (natural) languages. As such, NLP is related to the area of human–computer interaction. Many challenges in NLP involve natural language understanding, natural language generation, and machine learning. Text summarization is the process of distilling the most important information from a source (text) to produce an abridged version for a particular user or task. Automatic text summarization methods are greatly needed to address the ever-growing amount of text data available online to both better help discover relevant information and to consume the vast amount of text data available more efficiently."""

clean_text = preprocess_text(text)

keywords = get_most_frequent_words(clean_text, num_words=5)

summary = summarize_text(text, keywords)

print("Summary:")
print(summary)


