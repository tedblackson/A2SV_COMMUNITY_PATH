class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        transpose = [[0 for i in range(len(matrix))] for j in range(len(matrix[0]))]
        print(transpose)

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                transpose[col][row] = matrix[row][col]
        return transpose