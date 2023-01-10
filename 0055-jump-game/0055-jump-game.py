class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        maxIndex = 0
        
        for i, num in enumerate(nums):
            if i <= maxIndex:
                maxIndex = max(maxIndex, num + i)
        return True if maxIndex >= len(nums) - 1 else False

        
            
            
        