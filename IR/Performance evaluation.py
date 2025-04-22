from sklearn.metrics import precision_score, recall_score, f1_score, average_precision_score

y_true = [0, 1, 1, 0, 1]
y_scores = [0.1, 0.8, 0.6, 0.3, 0.9]

y_pred = [1 if score >= 0.5 else 0 for score in y_scores]

precision = precision_score(y_true, y_pred)
recall = recall_score(y_true, y_pred)
f1 = f1_score(y_true, y_pred)
avg_precision = average_precision_score(y_true, y_scores)

print("Precision:", round(precision, 2))
print("Recall:", round(recall, 2))
print("F1 Score:", round(f1, 2))
print("Average Precision:", round(avg_precision, 2))
