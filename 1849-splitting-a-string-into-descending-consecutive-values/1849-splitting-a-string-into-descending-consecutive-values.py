class Solution:
    def splitString(self, s: str) -> bool:
        
        ans = False
        max_value = int(s)
        n = len(s)
        
        def backtrack(prev, start):
            nonlocal ans
            
            #base case
            if start == n and prev != max_value:
                ans = True
                return
            
            for step in range(n):
                
                if start + step >= n:
                    continue
                
                cur = s[start: start + step + 1]
                # print('before', cur, end = ', ')
                
                cur = int(cur)
                # print('after', cur)
                
                if start == 0 or prev - cur == 1:
                    backtrack(cur, start + step + 1)
        
        backtrack(math.inf, 0)
        
        return ans
                
            
            
                
        
        
            
            