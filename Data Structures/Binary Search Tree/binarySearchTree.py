# Full fledged implementation of BInary Tree 

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

    def breadth_first_search(self):
        current_node = self.root
        result = []
        queue = []
        queue.append(current_node)
        while len(queue) > 0:
            current_node = queue.pop(0)
            result.append(current_node.data)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        return result

    def breadth_first_searchR(self, queue: list, result: list):
        if len(queue) == 0:
            return result

        current_node = queue.pop(0)
        result.append(current_node.data)
        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)
        return self.breadth_first_searchR(queue, result)

    def DFSinorder(self):
        return self._traverse_in_order(self.root, [])

    def DFSPreorder(self):
        return self._traverse_pre_order(self.root, [])

    def DFSPostorder(self):
        return self._traverse_post_order(self.root, [])

    def _traverse_in_order(self, node, result):
        if node is not None:
            self._traverse_in_order(node.left, result)
            result.append(node.data)
            self._traverse_in_order(node.right, result)
        return result

    def _traverse_pre_order(self, node, result):
        if node is not None:
            result.append(node.data)
            self._traverse_pre_order(node.left, result)
            self._traverse_pre_order(node.right, result)
        return result

    def _traverse_post_order(self, node, result):
        if node is not None:
            self._traverse_post_order(node.left, result)
            self._traverse_post_order(node.right, result)
            result.append(node.data)
        return result


# Example Usage:
bst = BinarySearchTree()
bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(3)
bst.insert(7)
bst.insert(9)

print("Inorder Traversal:", bst.DFSinorder())
print("Preorder Traversal:", bst.DFSPreorder())
print("Postorder Traversal:", bst.DFSPostorder())
print("BFS:", bst.breadth_first_search())