class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        queue , total, shortest = deque(), 0, math.inf
        
        for i, num in enumerate(nums):
            total += num
            shortest = min(shortest, i + 1) if total >= k else shortest
            current = []
            while queue and total - queue[0][0] >= k:
                current = queue.popleft()
            shortest = min(shortest, i - current[1]) if current else shortest
                
            while queue and queue[-1][0] > total:
                queue.pop()
            queue.append([total, i])
        return shortest if shortest != math.inf else - 1     