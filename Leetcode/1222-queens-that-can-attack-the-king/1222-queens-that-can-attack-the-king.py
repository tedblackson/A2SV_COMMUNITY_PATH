class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        
        queens = [tuple(queen) for queen in queens]
        queens = set(queens)
        
        directions = [[1,0], [-1, 0], [0,1], [0, -1], [1,1], [-1,-1], [-1, 1], [1, -1] ]
        checkQueens = []
        
        for direction in directions:
            curX = direction[0] + king[0]
            curY = direction[1] + king[1]

            while 0 <= curX < 8 and 0 <= curY < 8 :
                
                if (curX, curY) in queens:
                    checkQueens.append([curX, curY])
                    break
                curX += direction[0] 
                curY += direction[1] 
        
                
        return checkQueens
                
            