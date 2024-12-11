def bubblesort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

    return array

arr = bubblesort([1, 5, 4, 8, 3, 2, 12, 11, 10])
print(arr)