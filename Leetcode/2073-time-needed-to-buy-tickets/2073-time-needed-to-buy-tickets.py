class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        
        tickets = [(val, idx) for idx, val in enumerate(tickets)]
        queue = deque(tickets)
        print(queue)
        
        count = 0
        
        while deque:
            cur = queue.popleft()
            temp = cur[0] - 1
            count += 1

            if temp :
                queue.append((temp, cur[1]))
            elif cur[1] == k:
                break
        return count
        