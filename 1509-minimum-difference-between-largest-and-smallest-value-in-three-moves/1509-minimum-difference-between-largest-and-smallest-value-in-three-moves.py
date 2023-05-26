class Solution:
    def minDifference(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        
        left , right = 0, n - 1
        cnt = 3
        if n <= 3:
            return 0
        
        _min = float('inf')
        
        _min = min(_min, nums[n - 4] - nums[0]) # Remove all three largest
        _min = min(_min, nums[n - 3] - nums[1]) # Remove Two largest
        _min = min(_min, nums[n - 2] - nums[2]) # Remove One Largest
        _min = min(_min, nums[n - 1] - nums[3]) # Remove all Smallest
        
        return _min
        
        

        
        
            
            