class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data):
        new_node = Node(data)
        if not self.tail:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        if not self.head:
            return None
        dequeue_data = self.head.data
        self.head = self.head.next
        if not self.head:
            self.tail = None
        return dequeue_data

    def peek(self):
        if not self.head:
            return None
        return self.head.data

    def is_empty(self):
        return self.head is None

    def print_q(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


class Stack:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, x):
        self.q2.enqueue(x)
        while not self.q1.is_empty():
            self.q2.enqueue(self.q1.dequeue())
        self.q1, self.q2 = self.q2, self.q1  # Swap the queues

    def pop(self):
        if self.q1.is_empty():
            print("Stack is Empty.")
            return None
        return self.q1.dequeue()

    def top(self):
        if self.q1.is_empty():
            print("Stack is Empty.")
            return None
        return self.q1.peek()

    def empty(self):
        return self.q1.is_empty()
