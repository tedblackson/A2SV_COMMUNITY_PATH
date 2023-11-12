class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        
        @cache
        def dp(cur, buy, tran):

            if cur == n or tran <= 0:
                return 0
            if buy is False:

                one = -prices[cur] + dp(cur + 1, True, tran  -1)
                two = dp(cur + 1, False, tran)
            else:
                one = prices[cur] + dp(cur + 1, False, tran - 1)
                two = dp(cur + 1, True, tran)
            
            ans = max(one, two)
            return ans
        
        res = dp(0, False, 4)
        return res
            
            
            

        
            