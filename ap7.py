
def floyd_warshall(graph):
    V = len(graph)
    dist = [row[:] for row in graph]
    print(dist)
    for k in range(V):
        for i in range(V):
            for j in range(V):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist

def print_solution(dist):
    V = len(dist)
    for i in range(V):
        for j in range(V):
            if dist[i][j] == float("inf"):
                print("INF", end="\t")
            else:
                print(dist[i][j], end="\t")
        print()
if __name__ == "__main__":
    graph = [
        [0, 3, float("inf"), 7],
        [8, 0, 2, float("inf")],
        [5, float("inf"), 0, 1],
        [2, float("inf"), float("inf"), 0]
    ]
    shortest_paths = floyd_warshall(graph)
    print("Shortest paths between all pairs of vertices:")
    print_solution(shortest_paths)