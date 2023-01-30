class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        store = set()
        n = ceil(pow(c, 0.5))
        left = 0
        right = n
        
        while left <= right:
            total = left**2 + right**2
            
            if total < c:
                left += 1
            elif total > c:
                right -= 1
            else:
                return True
        return False
                
        
        
        
            
        
       
            