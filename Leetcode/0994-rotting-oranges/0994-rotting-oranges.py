class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        queue = deque()
        m , n = len(grid), len(grid[0])
        size = m * n
        visited = set()
        fruit = time = 0
        
        def inBound(row, col):
            return 0 <= row < m and 0 <= col < n
        for i in range(size):
            row , col = i// n , i % n
            if grid[row][col] != 0:
                fruit += 1
            if grid[row][col] == 2:
                queue.append((row, col))
                visited.add((row, col))
            
        
        temp =[]
        while queue:
            src = queue.popleft()
            
            for direction in directions:
                newRow = src[0] + direction[0]
                newCol = src[1] + direction[1]
                if inBound(newRow, newCol) and grid[newRow][newCol] == 1 and (newRow, newCol) not in visited:
                    visited.add((newRow, newCol))
                    temp.append((newRow, newCol))
            if not queue:
                if temp:
                    queue = deque(temp)
                    temp = []
                    time += 1
        return time if len(visited) == fruit else -1
                        
                        
            
            
            