class Graph:
    def __init__(self):
        self.number_of_nodes = 0
        self.adjacentList = {}

    def addVertex(self, node):
        # Check if the node already exists
        if node in self.adjacentList:
            print("Node already exists!")
            return
        
        # Initialize the adjacency list for the new node
        for key in self.adjacentList:
            self.adjacentList[key].append(0)  # Add new column (0) for existing nodes

        # Add the new node's adjacency list, initially all 0's
        self.adjacentList[node] = [0] * (self.number_of_nodes + 1)
        
        # Increment the node count
        self.number_of_nodes += 1
        print(f"Node '{node}' added.")

    def addEdge(self, node1, node2):
        # Ensure both nodes exist
        if node1 not in self.adjacentList or node2 not in self.adjacentList:
            print("One or both nodes do not exist!")
            return

        # Since the graph is undirected, we update both directions
        self.adjacentList[node1][node2] = 1
        self.adjacentList[node2][node1] = 1
        print(f"Edge added between '{node1}' and '{node2}'.")

    def showConnections(self):
        # Display the adjacency matrix representation of the graph
        for node, edges in self.adjacentList.items():
            print(f"{node}: {edges}")
