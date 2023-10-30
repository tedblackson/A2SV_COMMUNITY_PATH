class Solution:
    def repeatedStringMatch(self, haystack: str, needle: str) -> int:
        n, m= len(needle) // len(haystack), len(needle)
        
        choices = [haystack * n , haystack * (n + 1), haystack *(n + 2)]
        lps = self.preprocess(needle)
        
        for i, choice in enumerate(choices):
            if self.search(choice, needle, lps):
                return n + i
        return -1
        
        

        
    def search(self, haystack: str, needle: str, lps):
            
        n ,m , i, j  = len(haystack), len(needle), 0, 0
        
        while i < n:
            
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            elif j == 0:
                i += 1
            else:
                j = lps[j - 1]
            
            if j == m:
                return True
        return False
    
    def preprocess(self, needle):
        m = len(needle)
               
        lps = [0] * m
        prev , i = 0, 1
        while i < m:
            if needle[prev] == needle[i]:
                lps[i] = prev + 1
                prev += 1
                i += 1
            elif prev == 0:
                lps[i] = 0
                i += 1
            else:
                prev = lps[prev - 1]
        return lps