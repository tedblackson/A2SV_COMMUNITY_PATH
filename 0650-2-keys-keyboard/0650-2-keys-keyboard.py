class Solution:
    def minSteps(self, n: int) -> int:
        count = 0
        
        d = 2
        ans = 0
        while d * d <= n:
            
            while n > 0 and not(n % d):
                ans += d
                n //=d
            d += 1
        if n > 1:
            ans += n
        return ans
                
                
    
    
    