class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        n = len(nums)
        
        low = -1
        high = n
        
        while high > low + 1:
            
            mid = low + (high - low)//2
            
            if nums[mid] >= target:
                high = mid
            else:
                low = mid
                
        return high