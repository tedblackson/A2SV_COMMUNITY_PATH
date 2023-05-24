class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        _cols = len(mat[0])
        n = len(mat) * _cols
        zeros = []


        ans = [[math.inf] * _cols for _ in mat] 
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        def process_zeros():
            for i in range(n):
                _row, _col = i//_cols , i % _cols
                if mat[_row][_col] == 0 :
                    zeros.append((_row, _col))
        
        
        def inBound(row, col):
            return 0 <= row < len(mat) and 0 <= col < len(mat[0])
        
        process_zeros()
        queue = deque(zeros)
        
        visited, temp, level =  set() , [], 0
        
        
        while queue:
            src = queue.popleft()
            ans[src[0]][src[1]] = min (ans[src[0]][src[1]], level)
            
            for direction in directions:
                row = src[0] + direction[0]
                col = src[1] + direction[1]
                if inBound(row, col) and (row, col) not in visited:
                    temp.append((row, col))
                    visited.add((row, col))
                
            if not queue and temp:
                queue = deque(temp)
                temp = []   
                level += 1
        
         
        return ans
                
                
            