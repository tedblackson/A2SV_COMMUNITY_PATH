class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        cntA = cntB = 0
        n = len(costs)
        half = n //2
        costs.sort(reverse = True , key = lambda ele: abs(ele[0] - ele[1]))
        
        ans = 0
        
        for ele in costs:
            
            if cntB == half or  cntA < half and ele[0] <= ele[1]:
                cntA += 1
                ans += ele[0]
            else:
                ans += ele[1]
                cntB += 1
        return ans
        
        