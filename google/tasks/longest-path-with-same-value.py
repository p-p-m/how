import collections

class Node:
    def __init__(self, index, label):
        self.index = index
        self.label = label
        self.children = []

    @property
    def same_label_children(self):
        return [child for child in self.children if child.label == self.label]

    def __repr__(self):
        return '{}(label={})'.format(self.index, self.label)

    def __eq__(self, other):
        return self.index == other.index

    def __hash__(self):
        return self.index


class Solution:
    """
    @param A: as indicated in the description
    @param E: as indicated in the description
    @return: Return the number of edges on the longest path with same value.
    """
    def LongestPathWithSameValue(self, A, E):
        edges = self.as_edges(E)
        print('Edges:')
        print(edges)
        nodes = self.to_graph(A, edges)
        print('Nodes:')
        print(nodes)
        leafs = [node for node in nodes if len(node.same_label_children) == 1]
        print('Leafs:')
        print(leafs)
        if not leafs:
            return 0
        distances = [self.get_max_distance(leaf) for leaf in leafs]
        return max(distances)

    def batch(self, l):
        for i in range(0, len(l), 2):
            yield l[i: i+2]

    def as_edges(self, E):
        edges = collections.defaultdict(list)
        for edge, child in self.batch(E):
            edges[edge].append(child)
            edges[child].append(edge)
        return edges

    def to_graph(self, A, edges):
        nodes = [Node(index+1, label) for index, label in enumerate(A)]
        for index in range(1, len(A) + 1):
            node = nodes[index-1]
            node.children = [nodes[i-1] for i in edges[index]]
        return nodes

    def get_max_distance(self, leaf):
        nodes = [(leaf, 0)]
        visited = set()
        for node, level in nodes:
            for child in node.same_label_children:
                if child in visited:
                    continue
                nodes += [(child, level + 1)]
                visited.add(child)
        return max(level for _, level in nodes)


# solution = Solution()
# A = [1, 1, 1, 2, 2]
# E = [1, 2, 1, 3, 2, 4, 2, 5]

# print(solution.LongestPathWithSameValue(A, E))

node1 = Node(1, 1)
node2 = Node(2, 1)
node3 = Node(2, 2)

visited = {node1, node2}
print node3 in visited

