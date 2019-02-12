def get_breadth_first_nodes(root):
    nodes = []
    stack = [root]
    while stack:
        cur_node = stack[0]
        stack = stack[1:]
        nodes.append(cur_node)
        for child in cur_node.get_children():
            stack.append(child)
    return nodes


def get_depth_first_nodes_preorder(root):
    nodes = []
    stack = [root]
    while stack:
        cur_node = stack[0]
        stack = stack[1:]
        nodes.append(cur_node)
        for child in cur_node.get_rev_children():
            stack.insert(0, child)
    return nodes


def get_depth_first_nodes_postorder(root):
    nodes = []
    stack = [root]


########################################################################
class Node(object):
    def __init__(self, id_):
        self.id = id_
        self.children = []

    def __repr__(self):
        return "Node: [%s]" % self.id

    def add_child(self, node):
        self.children.append(node)

    def get_children(self):
        return self.children

    def get_rev_children(self):
        children = self.children[:]
        children.reverse()
        return children


root = Node(1)
second = Node(2)
root.add_child(second)
root.add_child(Node(3))
second.add_child(Node(4))
second.add_child(Node(5))

print get_depth_first_nodes_preorder(root)