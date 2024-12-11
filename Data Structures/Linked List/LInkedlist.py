class Node:
    """A class representing a single node in a linked list."""

    def __init__(self, data):
        self.data = data
        self.next = None  # Pointer to the next node


class LinkedList:
    """A class representing a singly linked list."""

    def __init__(self):
        self.head = None  # The head of the list

    def insert_at_beginning(self, data):
        """Insert a new node at the beginning of the list."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        """Insert a new node at the end of the list."""
        new_node = Node(data)
        if not self.head:  # If the list is empty
            self.head = new_node
            return
        current = self.head
        while current.next:  # Traverse to the end of the list
            current = current.next
        current.next = new_node

    def insert_at_index(self, index, data):
        new_node = Node(data)

        if index < 0:
            print("Enter a valid index")
            return

        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        current_index = 0

        while current and current_index < index - 1:
            current = current.next
            current_index += 1

        new_node.next = current.next
        current.next = new_node

    def delete_with_key(self, key):

        current = self.head

        if current and current.data == key:
            self.head = current.next
            current = None
            return

        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        if not current:
            print("Key is invalid")

        prev.next = current.next
        current = None

    def delete_at_index(self, index):
        # If the list is empty
        if not self.head:
            print("List is empty. Nothing to delete.")
            return

        # If the index is 0, delete the head node
        if index == 0:
            node_to_be_deleted = self.head
            self.head = self.head.next
            node_to_be_deleted.next = None
            return

        # Traverse the list to find the node before the one to be deleted
        current = self.head
        current_index = 0

        while current and current_index < index - 1:
            current = current.next
            current_index += 1

        # Check if we are out of bounds
        if not current or not current.next:
            print("Index out of bounds.")
            return

        # Delete the node at the given index
        node_to_be_deleted = current.next
        current.next = node_to_be_deleted.next
        node_to_be_deleted.next = None

    def print_list(self):
        """Print the linked list."""
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


linked_list = LinkedList()
