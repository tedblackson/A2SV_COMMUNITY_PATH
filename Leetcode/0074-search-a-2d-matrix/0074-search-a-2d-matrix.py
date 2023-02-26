class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) * len(matrix[0]) - 1
        col_num = len(matrix[0])
        
        while left <= right:
            mid = left + (right - left)//2  
            value = matrix[mid // col_num][mid % col_num]
            
            if value == target:
                return True
            elif target < value:
                right = mid - 1
            else:
                left = mid + 1
        return False
            
        
        