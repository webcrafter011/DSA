class Queue:
    def __init__(self):
        self.array = []

    def peek(self):
        return self.array[0]

    def enqueue(self, data):
        self.array.append(data)

    def dequeue(self):
        self.array.pop(0)
        
    def print_q(self):
        for i in self.array:
            print(i, end=' -> ')
        print("None")
        return

newq = Queue()
newq.enqueue(10)
newq.enqueue(20)
newq.enqueue(30)
newq.enqueue(40)
newq.dequeue()
newq.dequeue()
newq.print_q()