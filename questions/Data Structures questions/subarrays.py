class Solution(object):
    def maxSubArray(self, nums):

        maxSum = float("-inf")
        current_sum = 0
        for i in range(len(nums)):
            current_sum += nums[i]
            maxSum = max(current_sum, maxSum)
            if current_sum < 0:
                current_sum = 0
        return maxSum
