def swap(array, i, j):
    array[i], array[j] = array[j], array[i]
    return


def nextPermutation(array):
    pivot = -1
    for i in range((len(array) - 2), -1, -1):
        if array[pivot] > array[i]:
            swap(array, pivot, i)
            break
        else:
            pivot = pivot - 1
    else:
        array = array[::-1]
        
    return array


array = [3, 2, 1]
print(nextPermutation(array))
