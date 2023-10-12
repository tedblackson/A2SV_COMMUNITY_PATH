class Solution:
    def countOrders(self, n: int) -> int:

        MOD = 10**9 + 7

        res = 1
        spots = 2 * n
        for spot in range(spots, 1, -2):
            res *= spot * (spot - 1)//2
            res %= MOD

        return res %MOD
        
      

                
            
        