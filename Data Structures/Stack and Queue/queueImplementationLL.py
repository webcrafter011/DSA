# Implementation of Queues using Linked List

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
            print("Queue is empty. Cannot dequeue.")
            return None
        dequeued_data = self.head.data
        self.head = self.head.next
        if not self.head:  # If the queue becomes empty
            self.tail = None
        return dequeued_data

    def peek(self):
        if not self.head:
            print("Queue is empty. Nothing to peek.")
            return None
        return self.head.data

    def print_q(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
