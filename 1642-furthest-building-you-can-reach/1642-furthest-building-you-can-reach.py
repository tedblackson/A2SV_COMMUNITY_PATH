class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        total = 0
        largest = []
        
        for i in range(len(heights) -1 ):
            height = heights[i + 1] - heights[i]
            if height > 0 and len(largest) < ladders:
                heappush(largest, height)
                
            elif height > 0:
                if ladders:
                    val = heappop(largest)
                    heappush(largest, max(height, val))
                    val = min(height, val)
                else:
                    val = height
                
                if bricks - val >= 0:
                    bricks -= val
                else:
                    return i 
        return len(heights) - 1
            
        
            
        
            
            