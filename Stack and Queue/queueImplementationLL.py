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
        self.head = self.head.next
        return

    def peek(self):
        return self.head

    def print_q(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)
q.dequeue()
q.dequeue()
q.print_q()
