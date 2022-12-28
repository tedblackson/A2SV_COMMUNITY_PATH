class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        
        piles = [ -1 * pile for pile in piles]
        
        heapify(piles)
        
        for i in range(k):
            maxVal = heappop(piles)
            maxVal = floor(maxVal/2)
            heappush(piles, maxVal)
        
        return -1 * sum(piles)
            
            
            
        
        
        
        
        
        
        