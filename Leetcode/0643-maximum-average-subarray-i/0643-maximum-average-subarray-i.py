class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxsum = sum(nums[:k])
        totalSum = sum(nums[:k])
        start = 0
        for end in range(k, len(nums )):
            totalSum -= nums[start]
            totalSum += nums[end]
            start += 1
            maxsum = max(maxsum , totalSum)
        return maxsum/k