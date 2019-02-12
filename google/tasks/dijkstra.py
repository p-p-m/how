import functools


@functools.total_ordering
class Vertex:

    def __init__(self, index, distance):
        self.index = index
        self.distance = distance

    def __ne__(self, other):
        return self.index != other.index

    def __lt__(self, other):
        return self.distance < other.distance

    def __hash__(self):
        return hash(self.index)

    def __repr__(self):
        return 'V{}(d={})'.format(self.index, self.distance)


class Dijkstra:

    def __init__(self, graph):
        self.graph = graph
        self.spt = set()  # Shortest path tree
        self.vertexes = [Vertex(0, 0) if index == 0 else None for index in range(len(graph))]

    def get_min_vertex(self):
        """ Return vertex that has minimum distance and is not visited yet (not in SPT). """
        return min([vertex for vertex in self.vertexes if vertex is not None and vertex not in self.spt])

    def execute(self):
        while len(self.spt) < len(self.vertexes):
            min_vertex = self.get_min_vertex()
            self.spt.add(min_vertex)
            self.update_distances(min_vertex)
            self.print_spt()
            print('\n')

    def update_distances(self, root_vertex):
        """ Update distances of all adjastance vertixes of given vertix. """
        for index, distance in enumerate(self.graph[root_vertex.index]):
            if distance == 0:
                continue
            vertex = self.vertexes[index]
            if vertex is None:
                self.vertexes[index] = Vertex(index, root_vertex.distance + distance)
            elif vertex.distance > root_vertex.distance + distance:
                vertex.distance = root_vertex.distance + distance

    def print_spt(self):
        for vertex in self.spt:
            print(vertex)


graph = [
    [0, 4, 0, 0, 0, 0, 0, 8, 0],
    [4, 0, 8, 0, 0, 0, 0, 11, 0],
    [0, 8, 0, 7, 0, 4, 0, 0, 2],
    [0, 0, 7, 0, 9, 14, 0, 0, 0],
    [0, 0, 0, 9, 0, 10, 0, 0, 0],
    [0, 0, 4, 14, 10, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 2, 0, 1, 6],
    [8, 11, 0, 0, 0, 0, 1, 0, 7],
    [0, 0, 2, 0, 0, 0, 6, 7, 0]
];
dijkstra = Dijkstra(graph)
dijkstra.execute()
dijkstra.print_spt()

