class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        stones = [tuple(stone) for stone in stones] 
        n = len(stones)

        self.rep = {ele: ele for ele in stones}
        self.rank = {ele: 1 for ele in stones}
        component = n
        for i in range(n):
            for j in range(i + 1, n):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    if self.union(stones[i], stones[j]):
                        component -= 1
                        
        ans = n - component
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
            if self.rank[xrep] > self.rank[yrep]:
                self.rep[yrep] = xrep
                self.rank[xrep] += self.rank[yrep]
            
            else:
                self.rep[xrep] = yrep
                self.rank[yrep] += self.rank[xrep]
            
            return True
        return False
        
       
            