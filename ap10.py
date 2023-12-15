
from collections import defaultdict
def dijkstra(graph, source):
    distances = {vertex: float('infinity') for vertex in graph}
    visited = {vertex: False for vertex in graph}
    distances[source] = 0
    for _ in range(len(graph)):
        current_vertex = min((vertex for vertex in graph if not visited[vertex]), key=lambda vertex: distances[vertex])
        visited[current_vertex] = True
        for neighbor, weight in graph[current_vertex].items():
            potential_distance = distances[current_vertex] + weight
            if potential_distance < distances[neighbor]:
                distances[neighbor] = potential_distance
    return distances
def generator_graph():
    d=defaultdict(defaultdict)
    n=int(input('enter no. of joins:'))
    print('enter the joints in graph with cost ...................................')
    for i in range(n):
        start=input('starting node: ')
        end=input('end node :')
        c=int(input('enter cost'))
        d[start][end]=c
    print(d)
    return d
               
if __name__ == "__main__":
    graph=generator_graph()

    source = input('enter source node: ')
   
    shortest_distances = dijkstra(graph, source)
   
    print("Shortest distances from source vertex", source, "to all other vertices:")
    for vertex, distance in shortest_distances.items():
        print(f"To {vertex}: {distance}")