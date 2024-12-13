array1 = ['a', 'b', 'c', 'd']
array2 = ['x', 'b', 'd', 'e']

def checkForCommonCharacter(array1, array2):
    for i in range(len(array1)):  # Correctly iterate over indices
        for j in range(len(array2)):
            if array1[i] == array2[j]:
                return True  # Returns on first match
    return False  # Optional return if no match

result = checkForCommonCharacter(array1, array2)
print(result)
