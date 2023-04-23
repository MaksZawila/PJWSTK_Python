# Maksymilian Zawiła s25085 gr.24c
import heapq

def dijkstra(graph, start):
    distances = {v: float('inf') for v in graph}
    distances[start] = 0

    pq = [(0, start)]

    while pq:
        (dist, current) = heapq.heappop(pq)

        if dist > distances[current]:
            continue

        for neighbor, weight in graph[current].items():
            distance = dist + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

A, B, C, D, E = {}, {}, {}, {}, {}

A["B"] = 6
A["C"] = 3
A["D"] = 4
A["E"] = 1

B["A"] = 6
B["C"] = 1

C["A"] = 3
C["B"] = 1
C["D"] = 2
C["E"] = 1

D["A"] = 4
D["C"] = 2
D["E"] = 3

E["A"] = 1
E["C"] = 1
E["D"] = 3

graph = {
    "A": A,
    "B": B,
    "C": C,
    "D": D,
    "E": E
}

start = "B"

print(dijkstra(graph, start))
