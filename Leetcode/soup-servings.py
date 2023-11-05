class Solution:
    def soupServings(self, n: int) -> float:
        
        bound = ceil(n /25)
        
        @cache
        def dp(typeA, typeB):
            ans = 0
            if typeA <= 0 and typeB > 0:
                return 1
            elif typeA <= 0 and typeB <= 0:
                return 0.5
            elif typeB <= 0:
                return 0
            
            ans += dp(typeA - 4, typeB )
            ans += dp(typeA - 3, typeB - 1)
            ans += dp(typeA - 2, typeB - 2)
            ans += dp(typeA - 1, typeB - 3)
            
            return ans * 0.25
    
        for tot in range(1, bound + 1):
            if dp(tot, tot) > 1 - 1e-5:
                return 1.0
            
    
        return dp(bound, bound)
    
            
            