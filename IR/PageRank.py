# pagerank.py

def pagerank(graph, damping=0.85, num_iterations=10):
    N = len(graph)
    pr = {page: 1 / N for page in graph}  

    for i in range(num_iterations):
        new_pr = {}
        
        dangling_sum = sum(pr[page] for page in graph if len(graph[page]) == 0)
        
        for page in graph:
            rank_sum = 0
            for other_page in graph:
                if page in graph[other_page]:
                    rank_sum += pr[other_page] / len(graph[other_page])
            
            new_pr[page] = (1 - damping) / N
            new_pr[page] += damping * (rank_sum + dangling_sum / N)
        
        pr = new_pr

    return pr


graph = {
        'A': ['B', 'C', 'D'],
        'B': ['C', 'E'],
        'C': ['A', 'D'],
        'D': [],
        'E': []
}

pr_values = pagerank(graph)

print("Final PageRank values:")
for page, rank in pr_values.items():
    print(f"{page}: {rank:.4f}")


