import functools
import heapq


@functools.total_ordering
class Vertex:

    def __init__(self, index, distance):
        self.index = index
        self.distance = distance
        self.is_invalid = False

    def __ne__(self, other):
        return self.index != other.index

    def __lt__(self, other):
        return self.distance < other.distance

    def __hash__(self):
        return hash(self.index)

    def __repr__(self):
        s = 'V{}(d={})'.format(self.index, self.distance)
        if self.is_invalid:
            s += 'invalid'
        return s


class Dijkstra:

    def __init__(self, graph):
        self.graph = graph
        self.spt = set()  # Shortest path tree
        self.vertexes = [None] * len(graph)
        self.vertexes_heap = []
        self._add_vertex(0, 0)

    def get_min_vertex(self):
        """ Return vertex that has minimum distance and is not visited yet (not in SPT). """
        while True:
            vertex = heapq.heappop(self.vertexes_heap)
            if not vertex.is_invalid:
                return vertex

    def execute(self):
        while len(self.spt) < len(self.vertexes):
            min_vertex = self.get_min_vertex()
            self.spt.add(min_vertex)
            self.update_distances(min_vertex)

    def update_distances(self, root_vertex):
        """ Update distances of all adjastance vertixes of given vertix. """
        for index, distance in enumerate(self.graph[root_vertex.index]):
            if distance == 0:
                continue
            vertex = self.vertexes[index]
            if vertex is None:
                self._add_vertex(index, root_vertex.distance + distance)
            elif vertex.distance > root_vertex.distance + distance:
                # Invalidate previous vertex in the heap and add a new one.
                vertex.is_invalid = True
                self._add_vertex(index, root_vertex.distance + distance)

    def _add_vertex(self, index, value):
        vertex = Vertex(index, value)
        self.vertexes[index] = vertex
        heapq.heappush(self.vertexes_heap, vertex)

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

