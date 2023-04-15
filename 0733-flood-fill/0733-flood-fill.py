class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        n = len(image)
        m = len(image[0])
        
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visited = set()
        def inBound(row, col):
            return 0 <= row < n and 0 <= col < m
            
        
        def dfs(row, col, prev):
            visited.add((row, col))
            
            for direction in directions:
                new_row = direction[0] + row
                new_col = direction[1] + col
                
                if inBound(new_row, new_col) and image[new_row][new_col] == prev:
                    if (new_row, new_col) not in visited:
                        image[new_row][new_col] = color
                        dfs(new_row, new_col, prev)
        prev = image[sr][sc]
        image[sr][sc] = color
        dfs(sr, sc, prev)
        return image
                
                
                
            
            
            