class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        mapper1 = {}
        mapper2 = {}
        if len(s) != len(pattern):
            return False
        for char, word in zip(pattern , s):
            mapper1[char] = word
            mapper2 [word] = char
        
        countPattern = Counter(pattern)
        countStr = Counter(s)
        
        for char, word in zip(pattern, s):
            if countPattern[char] != countStr[word] or mapper1[char] != word or mapper2[word] != char:
                return False
        return True
        
            
            
        
        
        
    

            
        