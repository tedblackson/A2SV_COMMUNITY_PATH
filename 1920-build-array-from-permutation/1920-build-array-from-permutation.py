class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        
        size = max(nums) + 1
        ans = [0] * size
        
        for i, num in enumerate(nums):
            ans[i] = nums[num]
        return ans
        