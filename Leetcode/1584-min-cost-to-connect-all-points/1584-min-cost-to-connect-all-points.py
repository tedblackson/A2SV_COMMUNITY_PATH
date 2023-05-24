class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        points = [tuple(point) for point in points]
        
        self.rep = {point : point for point in points}
        self.size = {point: 1 for point in points}
        edges = set()
        
        for one in points:
            for two in points:
                if one != two:
                    dist = abs(one[0] - two[0]) + abs(one[1] - two[1])
                    edges.add((dist, min(one, two), max(one, two)))
                
        edges = list(edges)
        edges.sort()
        n = len(points)
        ans = 0
        
        minCostTree = set()
        for edge in edges:
            
            cost , one, two = edge
            if len(minCostTree) == n - 1:
                print('here')
                print(minCostTree)
                break

            if self.find(one) != self.find(two):
                
                minCostTree.add(edge)
                self.union(one, two)
                ans += cost
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
            
            if self.size[xrep] > self.size[yrep]:
                self.rep[yrep] = xrep
                self.size[xrep] += self.size[yrep]
            else:
                self.rep[xrep] = yrep
                self.size[yrep] += self.size[xrep]
            return True
        return False