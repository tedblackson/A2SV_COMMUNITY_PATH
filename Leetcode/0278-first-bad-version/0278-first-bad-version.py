# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        low = 0
        high = n
        best = n
        
        while low <= high:
            
            mid = low + (high - low)//2
            
            if isBadVersion(mid):
                best = min(mid, best)
                high = mid -1
            
            else:
                low = mid + 1
        return best
            
            
            
        
        
        

