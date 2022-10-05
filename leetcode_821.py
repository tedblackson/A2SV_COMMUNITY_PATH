class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        
        sumQueue = deque()
        sum = 0
        shortest = float('inf')
        
        for i in range(len(nums)):
            sum += nums[i]
            
            if sum >= k:
                shortest = min(shortest, i + 1)
            current = []
            while len(sumQueue) > 0 and sum - sumQueue[0][0] >= k :
                current = sumQueue.popleft()
            
            if len(current) > 0:
                shortest = min(shortest, i - current[1])
            
            
            while len(sumQueue) > 0 and sumQueue[-1][0] > sum :
                    sumQueue.pop()
            
            
            sumQueue.append([sum, i])
        
        return -1 if shortest == float('inf') else shortest
        
        
            
    
            
            
        
    
        