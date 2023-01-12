class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = top = 0
        right, bottom  = len(matrix[0]) - 1, len(matrix) - 1
        while top <= bottom:
            
            midVer = top + (bottom - top)//2
            
            if target >= matrix[midVer][left] and target <= matrix[midVer][right]:
                break
                     
            elif target > matrix[midVer][right]:
                top = midVer + 1
            else:
                bottom = midVer - 1 

        while left <= right:
            midHor = left + ( right - left)//2
            if target == matrix[midVer][midHor]:
                 return True
            elif target < matrix[midVer][midHor]:
                right = midHor - 1
            else:
                left = midHor + 1
        return False
           
