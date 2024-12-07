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
            print("Queue is Empty.")
            return
        dequeue_data = self.head.data
        self.head = self.head.next
        if not self.head:
            self.tail = None
        return dequeue_data

    def peek(self):
        if not self.head:
            print("List is Empty.")
            return
        return self.head

    def print_q(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# TODO:
# void push(int x) Pushes element x to the top of the stack.
# int pop() Removes the element on the top of the stack and returns it.
# int top() Returns the element on the top of the stack.
# boolean empty() Returns true if the stack is empty, false otherwise.


class Stack:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, x):
        self.q2.enqueue(x)

        while self.q1:
            self.q2.enqueue(self.q2.dequeue())
            
        self.q1, self.q2 = self.q2, self.q1
        

    def print_stack(self):
        
