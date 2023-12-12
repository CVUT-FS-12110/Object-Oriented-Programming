from typing import Optional


class SingletonTree(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Tree(metaclass=SingletonTree):

    def __init__(self):

        self.root: Optional[Node] = None

    def insert(self, value: int):

        node: 'Node' = Node(value)

        if not self.root:
            self.root = node
            return 1

        self.root.insert(node)


class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

    def insert(self, node: 'Node'):

        if self.value < node.value:
            if self.right is not None:
                self.right.insert(node)
            else:
                node.parent = self
                self.right = node

        elif self.value > node.value:
            if self.left is not None:
                self.left.insert(node)
            else:
                node.parent = self
                self.left = node

        else:
            pass

    def __repr__(self):
        return f"Our node: {self.value}"
    # parent


tree = Tree()
list_to_insert = [10, 13, 5, 11, 8]
for val in list_to_insert:
    tree.insert(val)

tree2 = Tree()
tree2.insert(1)

pass