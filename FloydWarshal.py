INF = float('inf')

def floyd_warshall(graph):
    num_vertices = len(graph)
    dist = [[INF] * num_vertices for _ in range(num_vertices)]

    for i in range(num_vertices):
        for j in range(num_vertices):
            dist[i][j] = graph[i][j]

    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist

# Example Usage
graph = [[0, 5, INF, 10],
         [INF, 0, 3, INF],
         [INF, INF, 0, 1],
         [INF, INF, INF, 0]]

shortest_paths = floyd_warshall(graph)
print("Shortest paths between all pairs of vertices:")
for row in shortest_paths:
    print(row)
