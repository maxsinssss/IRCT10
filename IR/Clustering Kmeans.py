from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# Insert your own data/documents
documents = [
"This is the first document.",
"This document is the second document.",
"And this is the third one.",
"Is this the first document?",
"The last document is here."
]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(documents)

num_clusters = 2 
n_init_value = 10 
kmeans = KMeans(n_clusters=num_clusters, n_init='auto')
kmeans.fit(X)

cluster_labels = kmeans.labels_
silhouette_avg = silhouette_score(X, cluster_labels)

print("Cluster labels:", cluster_labels)
print("Silhouette Score:",silhouette_avg)
