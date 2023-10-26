class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        _on = 2 ** 32 -1 

        
        _minScore = _on
        n = len(nums)
        
        
        for num in nums:
            _minScore &= num
        
        if _minScore != 0:
            return 1
        
        else:
            
            cnt = 0
            cur = _on
            
            for num in nums:
                cur &= num
                if cur == 0:
                    cnt += 1
                    cur = _on
            return cnt
            
            
                
            
        
        