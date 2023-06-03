class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        memo = [-1] * (amount + 1)
        memo[0] = 0
        
        for am in range(1, amount + 1):
            memo[am] = float('inf')
            for coin in coins:
                if am >= coin:
                    memo[am] = min(memo[am], memo[am - coin] + 1)
        
        
        return memo[amount] if memo[amount] != float('inf') else -1