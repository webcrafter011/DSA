def merge_sort(arr):
    if len(arr) <= 1:  # Base case: A single element is already sorted
        return arr
    
    # Split the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # Recursively sort each half
    sorted_left = merge_sort(left_half)
    sorted_right = merge_sort(right_half)
    
    # Merge the two sorted halves
    return merge(sorted_left, sorted_right)

def merge(left, right):
    merged = []
    i = j = 0
    
    # Compare elements from both halves and pick the smallest one
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    
    # Append any remaining elements from the left half
    while i < len(left):
        merged.append(left[i])
        i += 1
    
    # Append any remaining elements from the right half
    while j < len(right):
        merged.append(right[j])
        j += 1
    
    return merged