class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        @cache
        def dfs(cur, state):
            
            if cur >= n:
                return 0
            
            if cur == n -1:
                return 0 if state else nums[n - 1]
            
            one = nums[cur] + dfs(cur + 2, state)
            two = dfs(cur + 1, state)
            ans = max(one, two)
            return ans
        
        selected = nums[0] + dfs(2, True )
        unselected = dfs(1, False)
        
        ans = max(selected, unselected)
        return ans
        
            
            
            
            
        
        
            
        
        

                
            