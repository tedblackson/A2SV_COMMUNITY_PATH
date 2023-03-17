class Solution:
    def splitString(self, s: str) -> bool:
        ans = False
        max_val = int(s)
        n = len(s)
        def backtrack(prev, start):
            nonlocal ans
            if start == n  and prev != max_val:
                ans = True
                return 
            
            for step in range(n - start):
                
                cur = int(s[start: start + step +  1 ])
                
                if start == 0 or prev - cur == 1:
                    backtrack(cur, start + step + 1 )
                    
        backtrack(math.inf, 0)
        return ans
            
            
                
        
        
            
            