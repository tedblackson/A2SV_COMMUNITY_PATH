from collections import Counter, deque
import heapq


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        counted = Counter(tasks)
        taskCount = [-count for count in counted.values()]
        heapq.heapify(taskCount)
        queue = deque()
        time = 0
        
        while taskCount or queue:
            time += 1
            if taskCount:
                count = heapq.heappop(taskCount) + 1
                if count:
                    queue.append([count, time + n])
            if queue and queue[0][1] == time:
                    heapq.heappush(taskCount, queue.popleft()[0])
        return time