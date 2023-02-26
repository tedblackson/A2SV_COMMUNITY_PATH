class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        diagonals = defaultdict(set)
    
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                diagonals[col - row].add(matrix[row][col])
        count = len(list(filter(lambda x : len(x) != 1, diagonals.values())))
        
        return True if count == 0 else False
                