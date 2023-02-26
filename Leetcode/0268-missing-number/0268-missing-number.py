class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums = set(nums)

        for i in range(n+1):
            if not i in nums:
                return i
       
        
        