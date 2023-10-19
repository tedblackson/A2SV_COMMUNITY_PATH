class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m , n = len(word1), len(word2)
     
        memo = [[0 for _ in range(n + 1)]  for _ in range(m + 1)]
        
        def defaultOrInBound(row, col):
            
            if 0 <= row < m + 1 and 0 <= col < n + 1:
                return memo[row][col]
            
            return float('inf')
        
        if not (m and n):
            return m or n
        
        for i in range(m + 1):
            memo[i][0] = i
        for j in range(n + 1):
            memo[0][j]  = j
        
        for row in range(1, m + 1):
            for col in range(1, n + 1): 
    
                isNotEqual = word1[row -1] != word2[col - 1]
                
                optionA = defaultOrInBound(row -1, col)
                optionB = defaultOrInBound(row, col - 1)
                optionC = defaultOrInBound(row -1, col -1)
                
                if not isNotEqual:
                    memo[row][col] = optionC
                    
                else:
                    memo[row][col] = min(optionA, optionB, optionC) + 1
        
        return memo[m][n]
                
                
                
        
        
            
            