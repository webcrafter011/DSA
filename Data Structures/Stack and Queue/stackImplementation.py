# Visualisation of the stack as linked list
# node1 -> node2 -> node3 -> node4 -> None
# [TOP]


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.length = 0

    def peek(self):
        if self.top is None:
            print("Stack is empty")
            return None
        return self.top.data

    def push(self, data):
        # new_node -> node1 -> node2 -> node3 -> node4 -> None
        # [TOP]
        new_node = Node(data)
        if not self.top:
            self.top = new_node
            return None
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if not self.top:
            print("Stack is empty")
            return None
        self.top = self.top.next

    def print_stack(self):
        current = self.top
        first_iteration = True
        while current:
            if first_iteration:
                print(current.data, end=" -> [TOP]\n")
                first_iteration = False
                current = current.next
                continue
            else:
                print(current.data)
            current = current.next
