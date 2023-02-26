class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        maxIndex = 0
        profit = 0
        total = sum(gas) - sum(cost)
        
        for i, (g, c) in enumerate(zip(gas, cost)):
            profit += g - c
            if profit < 0:
                maxIndex = i + 1
                profit = 0
        
        return maxIndex if total >= 0 else -1
            