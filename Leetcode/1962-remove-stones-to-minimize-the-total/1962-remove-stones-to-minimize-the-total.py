class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-1 * pile for pile in piles]
        
        heapify(piles)
        
        while k > 0:
            val = heappop(piles)
            val = floor(val/2)
            if val:
                heappush(piles, val)
            k -=1 
        ans = sum(piles)
        return -1 * ans