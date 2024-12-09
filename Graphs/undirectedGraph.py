# Implementation of an undirected graph in python


class Graph:
    def __init__(self):
        self.number_of_nodes = 0
        self.adjacentList = {}

    def addVertex(self, node):
        # Check if the node already exists
        if node in self.adjacentList:
            print("Node already exists!")
            return
        array = [0] * self.number_of_nodes
        self.adjacentList[node] = array
        self.number_of_nodes += 1
        for key in self.adjacentList:
            if key != node:
                self.adjacentList[key].append(0)

    def addEdge(self, node1, node2):

        return
