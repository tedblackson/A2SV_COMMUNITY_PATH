class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def count(rate):
            count = 0
            
            for pile in piles:
                
                count += ceil(pile/rate)
        

            return count
        
        
        low = 1
        high = max(piles)
        best = high
        while low <= high:
            
            mid = low + (high - low)//2
            
            if count(mid) <= h:
                high = mid  - 1
            else:
                low = mid + 1
        return low
        