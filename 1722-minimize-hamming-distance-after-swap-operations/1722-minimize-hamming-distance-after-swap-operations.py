class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        self.rep = [i for i in range(n)]
        self.size = [1] * n
        
        for one, two in allowedSwaps:
            self.union(one, two)
            
        self.compressAll(n)
        
        repSource, repTarget = defaultdict(int), defaultdict(int)

        for i in range(n):
            repSource[(self.rep[i], source[i])] += 1
            repTarget[(self.rep[i], target[i])] += 1
            
        common  = 0
        
        for key in repSource:
            common += min(repSource[key], repTarget[key])
        return n - common
    
    
    def compressAll(self, n):
        for i in range(n):
            self.rep[i] = self.find(self.rep[i])
        
    def find(self, x):
        
        if x == self.rep[x]:
            return x
        
        self.rep[x] = self.find(self.rep[x])
        return self.rep[x]

    def union(self, x, y):
        
        xrep = self.find(x)
        yrep = self.find(y)
        
        if xrep != yrep:
            
            if self.size[xrep] > self.size[yrep]:
                self.rep[yrep] = xrep
                self.size[xrep] += self.size[yrep]
            else:
                self.rep[xrep] = yrep
                self.size[yrep] += self.size[xrep]
            return True
        return False
    