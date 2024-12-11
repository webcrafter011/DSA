def TwoSum(array, target):
    for i in range(len(array)):
        for j in range(i + 1, len(array)):  
            if array[i] + array[j] == target:
                return [i, j]
    return "No match found"  # Only return after checking all pairs


print(TwoSum([1, 3, 5, 8, 9], 11))
