class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        stones = [tuple(stone) for stone in stones] 
        
        self.rows = defaultdict(set)
        self.cols = defaultdict(set)
        
        for row, col in stones:
            self.rows[row].add((row, col))
            self.cols[col].add((row, col))
        
        self.rep = {ele: ele for ele in stones}
        self.rank = {ele: 1 for ele in stones}
        
        for ele1 in stones:
            for ele2 in stones:
                if ele1 != ele2 and (ele1[0] == ele2[0] or ele1[1] == ele2[1]):
                    self.union(ele1, ele2)
        
        counted = Counter(self.rep.values())
        print(counted)

        print(self.rep)

        ans = 0
        for key , val in counted.items():
            ans += val - 1
        return ans
        
        
    def find(self, x):
        
        if x == self.rep[x]:
            return x
        
        self.rep[x] = self.find(self.rep[x])
        return self.rep[x]
    
    
    def union(self, x, y):
        
        xrep = self.find(x)
        yrep = self.find(y)
        
        
        if self.rank[xrep] > self.rank[yrep]:
            self.rep[yrep] = xrep
        
        elif self.rank[xrep] < self.rank[yrep]:
            self.rep[xrep] = yrep
        
        else:
            self.rep[yrep] = xrep
            self.rank[xrep] += 1
            