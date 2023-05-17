class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        self.rep = {char: char for char in s1}
        
        for char in s2:
            if char not in self.rep:
                self.rep[char] = char
        
        
        for first, second in zip(s1, s2):
            self.union(first, second)
        

        ans = ''
        for char in baseStr:
            if char in self.rep:

                ans += self.find(char)
            else:
                ans += char
        return ans

        
        
    def find(self, x):
        
        if x == self.rep[x]:
            return x
        
        self.rep[x] = self.find(self.rep[x])
        
        return self.rep[x]
        
    def union(self, x, y):
        
        xrep = self.find(x)
        yrep = self.find(y)
        
        if xrep != yrep:
            if xrep < yrep:
                self.rep[yrep] = xrep
            else:
                self.rep[xrep] = yrep
            
    
    
            