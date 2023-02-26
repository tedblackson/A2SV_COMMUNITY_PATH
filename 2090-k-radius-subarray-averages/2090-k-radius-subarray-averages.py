class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        ans = [-1] * len(nums)
        n = 2 * k + 1
        
        total = sum(nums[:n])
        if 0 <= n - k - 1 < len(nums) and n <= len(nums):
            ans[n - k - 1] = total//n 
        start = 0
        for end in range(n, len(nums)):
            total += nums[end]
            total -= nums[start]
            start += 1
            if 0 <= end - k < len(nums) :
                ans[end - k ] = total//n 
        return ans