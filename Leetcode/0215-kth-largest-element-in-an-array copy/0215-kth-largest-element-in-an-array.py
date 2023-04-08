class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        _min = min(nums)
        _max = max(nums)
        _range = _max - _min + 1
        
        counted = [0] * _range
        
        for ele in nums:
            counted[ele - _min] += 1
            
        for i in range(len(counted) - 1, -1, -1):
            
            while counted[i] > 0 and k > 0:
                counted[i] -= 1
                k -= 1
            if k == 0:
                return i + _min
        
            
        