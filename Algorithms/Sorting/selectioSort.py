def selectionSort(array) -> list:
    n = len(array)
    # outer loop to take iterate repeatedly until sorted
    for i in range(n):
        smallest_index = i
        # inner loop to sort via finding the smalled element every time
        for j in range(i + 1, n):
            if array[j] < array[smallest_index]:
                smallest_index = j
            array[i], array[smallest_index] = array[smallest_index], array[i]
                
    return array
            
