class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        
        n = len(satisfaction)
        visited = set()
        satisfaction.sort()
        
        @cache
        def dp(time, cur):
            
            if  cur == n:
                return 0
            take = time * satisfaction[cur] + dp(time + 1, cur + 1)
            notTake = dp(time , cur + 1)
            _max = max(take, notTake)

            return _max
        
        return dp(  1, 0)
        
        
        
        
        
        
       
        
        
        