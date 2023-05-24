class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        
        n = len(s)
        collected = defaultdict(list)
        
        self.rep = [i for i in range(n)]
        self.size = [1] * n
        
        for first, second in pairs:
            self.union(first, second)
        
        for i in range(n):
            self.rep[i] = self.find(self.rep[i])
            collected[self.rep[i]].append(s[i])
        
        for key in collected:
            collected[key].sort(reverse = True)
        
        ans = ''
        for i in range(n):
            ans += collected[self.rep[i]].pop()
        
        return ans
            

    
    def find(self, x):
       
        if x == self.rep[x]:
            return x
        
        self.rep[x] = self.find(self.rep[x])
        return self.rep[x]
    
    def union(self, x ,y):
        
        xrep = self.find(x)
        yrep = self.find(y)
        
        if self.size[xrep] > self.size[yrep]:
            self.rep[yrep] = xrep
            self.size[xrep] += self.size[yrep]
        
        else:
            self.rep[xrep] = yrep
            self.size[yrep] += self.size[xrep]
                    