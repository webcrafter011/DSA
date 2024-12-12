def quick_sort(arr):
    if len(arr) <= 1:  # Base case: a list of 0 or 1 elements is already sorted
        return arr
    else:
        # Choose a pivot (typically the last element)
        pivot = arr[-1]
        # Partition the array into elements less than the pivot and greater than or equal to the pivot
        less_than_pivot = [x for x in arr[:-1] if x <= pivot]
        greater_than_pivot = [x for x in arr[:-1] if x > pivot]
        # Recursively sort partitions and combine them
        return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)

    
