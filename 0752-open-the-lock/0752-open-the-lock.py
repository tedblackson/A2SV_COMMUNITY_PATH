class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        initial = "0000"
        level = 0
        visited = set()
        directions = [-1, 1]
        queue = deque()
        queue.append(initial)
        temp = []
        if initial in deadends:
            return -1
        while queue:
            
            src = queue.popleft()
            if src == target:
                return level
            for i in range(4):
                for direction in directions:
                    cur = int(src[i]) + direction
                    key = cur if cur >= 0 else 9
                    key = key if key <= 9 else 0 
                    child = src[:i] + str(key) + src[i + 1:]

                
                    if child not in visited and child not in deadends:
                        temp.append(child)
                        visited.add(child)
            if not queue and temp:
                queue = deque(temp)
                # print(queue)
                temp = []
                level += 1
        return -1
                
                        
            
        
        
