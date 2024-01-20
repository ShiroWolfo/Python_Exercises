class Graph:
    def __init__(self, graph_dict=None):
        self.__graph_dict = graph_dict or {}

    def vertices(self):
        return list(self.__graph_dict.keys())

    def edges(self):
        edges = []
        for vertex, neighbors in self.__graph_dict.items():
            for neighbor in neighbors:
                if {neighbor, vertex} not in edges:
                    edges.append({vertex, neighbor})
        return edges

    def add_vertex(self, vertex):
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = set()

    def add_edge(self, edge):
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge)
        if vertex1 in self.__graph_dict:
            self.__graph_dict[vertex1].add(vertex2)
        else:
            self.__graph_dict[vertex1] = {vertex2}
        if vertex2 in self.__graph_dict:
            self.__graph_dict[vertex2].add(vertex1)
        else:
            self.__graph_dict[vertex2] = {vertex1}

    def __str__(self):
        result = "Vertices: " + ", ".join(self.vertices()) + "\n"
        result += "Edges: "
        for edge in self.edges():
            result += str(list(edge)) + ", "
        return result.rstrip(", ")


# Przykładowe użycie klasy Graph
graph = Graph()
graph.add_vertex("A")
graph.add_vertex("B")
graph.add_vertex("C")
graph.add_vertex("D")
graph.add_edge(("A", "B"))
graph.add_edge(("B", "C"))
graph.add_edge(("C", "D"))
graph.add_edge(("D", "A"))

print(graph)
