def insertionSort(array): 
    for i in range(1, len(array)):
    # Starting the iteration from the second index, because there is no point in comparing the first element with itself
    
        key = array[i]
        j = i - 1
        
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        
        # Inserting the key at the correct position
        array[j + 1] = key
        
    return array

array = [12, 11, 13, 5, 6]
print(insertionSort(array))

# Visual explaination for better understanding 
# Let's visualize the Insertion Sort step by step using the array arr = [12, 11, 13, 5, 6]. Here's how the sorting process works:

# Initial Array
# [12, 11, 13, 5, 6]
# Step 1: i = 1 (Key = 11)
# key = 11, j = 0.
# Compare key (11) with arr[j] (12). Since 11 < 12, shift 12 to the right (arr[j + 1] = arr[j]).
# Now, j = -1, so we stop and insert key at arr[j + 1].
# Array after Step 1:

# [11, 12, 13, 5, 6]
# Step 2: i = 2 (Key = 13)
# key = 13, j = 1.
# Compare key (13) with arr[j] (12). Since 13 > 12, no shifting is needed.
# Insert key in place (it’s already in the correct position).
# Array after Step 2:

# [11, 12, 13, 5, 6]
# Step 3: i = 3 (Key = 5)
# key = 5, j = 2.
# Compare key (5) with arr[j] (13). Since 5 < 13, shift 13 to the right.
# j = 1. Compare key (5) with arr[j] (12). Since 5 < 12, shift 12 to the right.
# j = 0. Compare key (5) with arr[j] (11). Since 5 < 11, shift 11 to the right.
# j = -1, so we stop and insert key at arr[j + 1].
# Array after Step 3:

# [5, 11, 12, 13, 6]
# Step 4: i = 4 (Key = 6)
# key = 6, j = 3.
# Compare key (6) with arr[j] (13). Since 6 < 13, shift 13 to the right.
# j = 2. Compare key (6) with arr[j] (12). Since 6 < 12, shift 12 to the right.
# j = 1. Compare key (6) with arr[j] (11). Since 6 < 11, shift 11 to the right.
# j = 0. Compare key (6) with arr[j] (5). Since 6 > 5, stop shifting.
# Insert key at arr[j + 1].
# Array after Step 4:

# [5, 6, 11, 12, 13]


# Final Sorted Array
# [5, 6, 11, 12, 13]
