def MaxSubnums(nums):
    maxSum = float("-inf")  # Start with the smallest possible number
    length = len(nums)

    for i in range(length):  # Starting index of the subnums
        sum = 0
        for j in range(i, length):  # Ending index of the subnums
            sum += nums[j]  # Add the current element to the sum
            if sum > maxSum:  # Update maxSum if a larger sum is found
                maxSum = sum

    return maxSum


print(MaxSubnums([5, 4, -1, 7, 8]))
