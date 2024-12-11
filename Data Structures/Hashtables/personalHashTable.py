class hashTable:

    def __init__(self, size):
        self.data = [None] * size

    def _hash(self, key):
        hash_value = 0
        for i, char in enumerate(key):
            hash_value = (hash_value + ord(char) * i) % len(self.data)
        return hash_value

    def set(self, key, value):
        """
        Method to add a key-value pair to the hash table.
        """
        address = self._hash(key)
        if not self.data[address]:  # If the bucket is empty, initialize it
            self.data[address] = []
        self.data[address].append([key, value])  # Append the key-value pair
        print(self.data)
        return self.data

    def get(self, key):
        address = self._hash(key)
        currentBucket = self.data[address]
        if currentBucket:
            for pair in currentBucket:
                if pair[0] == key:
                    return pair[1]
        return None


myHashTable = hashTable(5)
myHashTable.set("grapes", 1000)
myHashTable.set("apple", 1564560)
myHashTable.set("pineapple", 1000)

print(myHashTable.get("apple"))
