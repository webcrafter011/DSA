def maxSubArray(array):
    maxSum = float("-inf")
    currentSum = 0

    for num in array:
        currentSum = max(num, currentSum + num)

        maxSum = max(maxSum, currentSum)

    return maxSum


print(maxSubArray([1, 2, -5, 4, -1, 2, 1, -5, 4]))
