class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [0] * (n + 3)

        
        for i in range(n + 1):
            if i < n:
                memo[i] = nums[i] + max(memo[i -2], memo[i - 3])
            elif i ==n:
                memo[i] = max(memo[i -1], memo[i - 2])
                
                        
        return memo[n]
            
        
        
        