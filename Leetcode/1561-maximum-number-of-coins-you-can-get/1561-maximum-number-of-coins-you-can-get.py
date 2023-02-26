class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        ans = left = 0
        right = len(piles) - 2
        piles.sort()
        
        while left < right:
            ans += piles[right]
            right -= 2
            left += 1
        return ans
        