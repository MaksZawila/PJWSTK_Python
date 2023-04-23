# Maksymilian Zawiła s25085 gr.24c
import heapq


class Graph:
    def __init__(self, graph_dict=None):
        if graph_dict is None:
            graph_dict = {}
        self.graph_dict = graph_dict

    def vertices(self):
        return list(self.graph_dict.keys())

    def edges(self):
        return self.__generate_edges()

    def add_vertex(self, vertex):
        if vertex not in self.graph_dict:
            self.graph_dict[vertex] = {}

    def add_edge(self, edge):
        edge = set(edge)
        vertex1, vertex2, weight = tuple(edge)
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)
        self.graph_dict[vertex1][vertex2] = weight
        self.graph_dict[vertex2][vertex1] = weight

    def __generate_edges(self):
        edges = []
        for vertex in self.graph_dict:
            for neighbour, weight in self.graph_dict[vertex].items():
                if (neighbour, vertex, weight) not in edges:
                    edges.append((vertex, neighbour, weight))
        return edges


class Dijkstra:
    def __init__(self, graph, start):
        self.graph = graph
        self.start = start
        self.distances = {v: float('inf') for v in graph.vertices()}
        self.distances[start] = 0
        self.queue = [(0, start)]

    def shortest_path(self):
        while self.queue:
            (dist, current) = heapq.heappop(self.queue)

            if dist > self.distances[current]:
                continue

            for neighbour, weight in self.graph.graph_dict[current].items():
                distance = dist + weight

                if distance < self.distances[neighbour]:
                    self.distances[neighbour] = distance
                    heapq.heappush(self.queue, (distance, neighbour))

        return self.distances


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

graph_dict = {
    "A": A,
    "B": B,
    "C": C,
    "D": D,
    "E": E
}
graph = Graph(graph_dict)

start = "A"
dijkstra = Dijkstra(graph, start)

print(dijkstra.shortest_path())
