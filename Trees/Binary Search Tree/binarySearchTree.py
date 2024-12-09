import json

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = Node(data)
        if not self.root:
            self.root = new_node
            return

        current = self.root
        while current:
            if data < current.data:
                if not current.left:
                    current.left = new_node
                    return
                current = current.left
            elif data > current.data:
                if not current.right:
                    current.right = new_node
                    return
                current = current.right
            else:
                print("This value already exists in the BST! Enter valid data.")
                return

    def lookup(self, data):
        current = self.root
        while current:
            if data < current.data:
                current = current.left
            elif data > current.data:
                current = current.right
            else:
                print("Node was found")
                return True
        print("Node was not found")
        return False


def traverse(node):
    if node is None:
        return None
    return {
        "value": node.data,
        "left": traverse(node.left),
        "right": traverse(node.right),
    }


def print_tree(node, level=0, prefix="Root: "):
    if node is not None:
        print(" " * (level * 4) + prefix + str(node.data))
        if node.left or node.right:  # Only recurse if there are children
            print_tree(node.left, level + 1, "L--- ")
            print_tree(node.right, level + 1, "R--- ")


# Example Usage:
bst = BinarySearchTree()
bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(3)
bst.insert(7)
bst.insert(9)
bst.insert(5)


print_tree(bst.root)

