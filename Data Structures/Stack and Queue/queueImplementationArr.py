class Queue:
    def __init__(self):
        # Initializes an empty queue using a list
        self.array = []

    def peek(self):
        if len(self.array) > 0:
            return self.array[0]
        return None  # Return None if the queue is empty

    def enqueue(self, data):
        self.array.append(data)

    def dequeue(self):
        if len(self.array) > 0:
            return self.array.pop(0)
        return None  # Return None if the queue is empty

    def print_q(self):
        for i in self.array:
            print(i, end=' -> ')
        print("None")
