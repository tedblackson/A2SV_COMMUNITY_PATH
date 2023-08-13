class Solution:
    def racecar(self, target: int) -> int:
        queue = deque([(1, 0, 0)])
        visited = set()
        
        
        while queue:
            speed, pos, steps = queue.popleft()
            
            if pos == target: return steps
            
            if (speed, pos) not in visited:
                visited.add((speed, pos))
                
                queue.append((speed * 2, pos + speed, steps + 1))
                
                if pos + speed > target and speed > 0:
                    speed = -1
                elif pos + speed < target and speed < 0:
                    speed = 1
                queue.append((speed, pos,  steps + 1))
                
        return steps