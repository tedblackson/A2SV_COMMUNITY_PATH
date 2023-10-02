class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m = len(dungeon)
        n = len(dungeon[0])
        
        
        dp = [[0 for _ in range(n)]  for _  in range(m)]
        dp[-1][-1] = dungeon[-1][-1]

        def inBound(row, col):
            return 0 <= row < m and 0 <= col < n


        for i in range(m -1, -1, -1 ):
            for j in range(n -1, -1 ,-1 ):
                
                cur = -math.inf
                cur = max(cur, dp[i][j + 1]) if inBound(i , j + 1) else cur
                cur = max(cur, dp[i + 1][j]) if inBound(i + 1, j) else cur
                

                cur = cur + dungeon[i][j] if cur != -math.inf else dungeon[i][j]
                dp[i][j] = cur if cur < 0 else 0
            
        return -1 * dp[0][0] + 1






        

        

   
            
      

                
            

