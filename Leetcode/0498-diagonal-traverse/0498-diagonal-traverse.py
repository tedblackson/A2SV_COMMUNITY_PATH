class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        endRow , endCol = len(mat) - 1, len(mat[0]) - 1
        curRow = curCol = 0
        
        upDiagonal = True
        res = []
        while curRow != endRow or curCol != endCol:
            res.append(mat[curRow][curCol])
            if upDiagonal and curRow - 1 < 0 and curCol + 1 <= endCol:
                curCol += 1
                upDiagonal = False
            elif upDiagonal and curCol + 1 > endCol:
                curRow +=  1
                upDiagonal = False
            elif not upDiagonal and curCol - 1  < 0 and curRow + 1 <=  endRow:
                curRow += 1
                upDiagonal = True
            elif not upDiagonal and curRow + 1 > endRow:
                curCol +=1 
                upDiagonal = True
            elif upDiagonal:
                curCol +=1 
                curRow -= 1
            else:
                curCol -= 1
                curRow += 1
        res.append(mat[endRow][endCol])
        return res
        

            
            

            
            
            
            
            
        return res