class Solution:
    def longestPrefix(self, s: str) -> str:
        n = len(s)
        
        lps = [0] * n
        prev , i = 0, 1
        
        while i < n :
            if s[prev] == s[i]:
                lps[i] = prev + 1
                i += 1
                prev += 1
            elif prev == 0:
                lps[i] = 0
                i += 1
            else:
                prev = lps[prev  - 1]
        
        

        return s[:lps[-1]]
            
        
        
        
                
        
                
            