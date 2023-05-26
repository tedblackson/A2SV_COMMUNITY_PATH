class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit = 0
        n = len(prices)
        buy = sell = 0

        while sell < n:
            if sell + 1 < n and prices[sell] < prices[sell + 1]:
                sell += 1
            else:
                profit += prices[sell] - prices[buy]
                sell += 1
                buy = sell
            
        return profit
            