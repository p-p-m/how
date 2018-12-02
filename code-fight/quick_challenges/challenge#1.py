# class Node:

#     def __init__(self, value, parent=None):
#         self.value = value
#         self.children = []
#         self.parent = parent

#     def switch_with_parent(self):
#         self.children.append(self.parent)
#         grandparent = self.parent.parent
#         self.parent.parent = self
#         self.parent = grandparent

#     def __repr__(self):
#         return 'N{}-P{}'.format(self.value, self.parent.value)

#     def __eq__(self, other):
#         return self.value == other.value

#     def __ne__(self, other):
#         return self.value != other.value


# class Tree:

#     def __init__(self, root_value):
#         self.root_value = root_value
#         self.root = Node(root_value)
#         self.root.parent = self.root
#         self.nodes = {root_value: self.root}

#     def add_node(self, parent_value, value):
#         parent = self.nodes[parent_value]
#         node = Node(value, parent)
#         parent.children.append(node)
#         self.nodes[value] = node

#     def __repr__(self):
#         to_print = [(0, self.nodes[self.root_value])]
#         for layer, node in to_print:
#             to_print += [(layer + 1, child) for child in node.children]
#         return str(to_print)

#     def change_root(self, new_root_value):
#         new_root = self.nodes[new_root_value]
#         new_root.switch_with_parent()

#     def to_list(self):
#         result = [None] * len(self.nodes)
#         for node in self.nodes.values():
#             result[node.value] = node.parent.value
#         return result

#     @classmethod
#     def from_list(self, l):
#         tree = Tree(l[0])
#         for index, el in enumerate(l[1:], start=1):
#             tree.add_node(el, index)
#         return tree


# tree = Tree.from_list([0, 0, 0, 1, 1, 1, 2, 2, 7])
# print tree
# tree.change_root(7)
# print tree
# print tree.to_list()


origin = [3, 3, 2, 2, 0]
origin_root = next(value for index, value in enumerate(origin) if index == value)
result = origin[:]
value = 0

result[value] = value

while value != origin[0]:
    previous_parent = origin[value]
    result[previous_parent] = value
    value = previous_parent

# previous_parent = origin[value]
# result[previous_parent] = value


# def switch(value):
#     previous_parent = origin[value]
#     result[previous_parent] = value
#     return previous_parent, value


# node, value = new_root, new_root
# while value != 0:
#     print node, value
#     node, value = switch(value)

# switch(value)

print result
