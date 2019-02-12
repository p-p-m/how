import functools


@functools.total_ordering
class Vertex:

    def __init__(self, index, key, parent=None):
        self.index = index
        self.key = key
        self.parent = parent

    def __ne__(self, other):
        return self.index != other.index

    def __lt__(self, other):
        return self.key < other.key

    def __hash__(self):
        return hash(self.index)

    def __repr__(self):
        if self.parent:
            return 'V{} -{}-> V{}'.format(self.parent.index, self.key, self.index)
        return 'Start V{}'.format(self.index, self.key)


class Prims:

    def __init__(self, graph):
        self.graph = graph
        self.mst = set()  # minimum spaning tree
        self.vertexes = [Vertex(0, 0) if index == 0 else None for index in range(len(graph))]

    def get_min_vertex(self):
        return min([vertex for vertex in self.vertexes if vertex is not None and vertex not in self.mst])

    def execute(self):
        while len(self.mst) < len(self.vertexes):
            min_vertex = self.get_min_vertex()
            self.mst.add(min_vertex)
            self.update_adjacent(min_vertex)

    def update_adjacent(self, root_vertex):
        for index, distance in enumerate(self.graph[root_vertex.index]):
            if distance == 0:
                continue
            vertex = self.vertexes[index]
            if vertex is None:
                self.vertexes[index] = Vertex(index, key=distance, parent=root_vertex)
            elif vertex.key > distance:
                vertex.key = distance
                vertex.parent = root_vertex

    def print_mst(self):
        for vertex in self.mst:
            print(vertex)


graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0],
]
prims = Prims(graph)
prims.execute()
prims.print_mst()
