
class Node():

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

    def __repr__(self):
        return str(self.data)

class Heap():

    def __init__(self, root):
        self.root = root

    def try_to_add(self, root, node):
        if not root.left:
            root.left = node
            node.parent = root
            return True
        elif not root.right:
            root.right = node
            node.parent = root
            return True
        else:
            return False

    def add(self, new_node):
        added = False
        nodes = [self.root, ]
        while not added:
            for node in nodes:
                added = self.try_to_add(node, new_node)
                if added:
                    break
            nodes = self.get_children(nodes)


        node = new_node
        while True:
            node, parent = node, node.parent
            if node.data > parent.data:
                parent.data, node.data = node.data, parent.data
                node = parent
            else:
                break
            if parent.parent is None:
                break
            


    def get_children(self, parents):
        children = []
        for parent in parents:
            if parent.left:
                children.append(parent.left)
            if parent.right:
                children.append(parent.right)
        return children

    def __repr__(self):
        output = ""
        nodes = [self.root, ]
        while nodes:
            output += " ".join([str(node) for node in nodes])
            output += "\n"
            nodes = self.get_children(nodes)
        return output


h = Heap(Node(10))

for n in range(1,20):
    print(f"============= added: {n}")
    h.add(Node(n))
    print(h)

