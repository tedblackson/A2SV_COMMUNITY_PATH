class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        
        n = len(num)
        ans = False
        if n < 3:
            return False
        
        
        def backtrack(prev1, prev2, start, count):
            nonlocal ans

            if ans == True:
                return
            
            if start >= n:
               
                if prev1 != math.inf and prev2 != math.inf and count > 2 and len(prev1) == len(str(int(prev1))) and len(prev2) == len(str(int(prev2))):
                    
                    
                    ans = True 
                return
            
            
            for step in range(n - start):
                cur = num[start: start + step + 1]
                
                
                if prev1 == math.inf or prev2 == math.inf or int(prev1) + int(prev2) == int(cur) and len(prev1) == len(str(int(prev1))) and len(prev2) == len(str(int(prev2))) :
                    
                    backtrack(prev2, cur, start + step + 1 , count + 1)
        backtrack(math.inf,math.inf,  0, 0)
        
        return ans
                
                
                
                
                
                
            
            