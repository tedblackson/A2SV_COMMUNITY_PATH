class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        curSum = 0
        maxSum = -math.inf
        
        for num in nums:
            curSum += num
            maxSum = max(curSum, maxSum)
            curSum = 0 if curSum < 0 else curSum
        return maxSum