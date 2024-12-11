# This is the implementation of queues with the help of stacks


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # Pointer to the next node


class Stack:
    def __init__(self):
        self.top = None  # Pointer to the top of the stack

    def spush(self, data):
        """Add an item to the top of the stack."""
        new_node = Node(data)
        new_node.next = self.top  # Link the new node to the current top
        self.top = new_node  # Update the top to the new node

    def spop(self):
        """Remove and return the top item of the stack."""
        if self.is_empty():
            print("Stack is empty. Cannot pop.")
            return None
        popped_data = self.top.data  # Get the data from the top node
        self.top = self.top.next  # Update the top to the next node
        return popped_data

    def speek(self):
        """Return the top item of the stack without removing it."""
        if self.is_empty():
            print("Stack is empty. Nothing to peek.")
            return None
        return self.top.data

    def sis_empty(self):
        """Check if the stack is empty."""
        return self.top is None

    def display(self):
        """Display all elements in the stack."""
        current = self.top
        stack_contents = []
        while current:
            stack_contents.append(current.data)
            current = current.next


# TODO :-
# void push(int x) Pushes element x to the back of the queue.
# int pop() Removes the element from the front of the queue and returns it.
# int peek() Returns the element at the front of the queue.
# boolean empty() Returns true if the queue is empty, false otherwise.


class Queue:
    def __init__(self):
        self.input = Stack()
        self.output = Stack()

    def push(self, x):
        """Push element x to the back of the queue."""
        self.input.spush(x)

    def pop(self):
        """Remove the element from the front of the queue and return it."""
        if self.output.sis_empty():  # Check if output stack is empty
            while not self.input.sis_empty():  # Transfer elements to output stack
                self.output.spush(self.input.spop())
        return self.output.spop()  # Pop from output stack and return the value

    def peek(self):
        """Return the element at the front of the queue."""
        if self.output.sis_empty():  # Check if output stack is empty
            while not self.input.sis_empty():  # Transfer elements to output stack
                self.output.spush(self.input.spop())
        return self.output.speek()  # Peek the top of output stack

    def empty(self):
        """Return true if the queue is empty, false otherwise."""
        return self.input.sis_empty() and self.output.sis_empty()
