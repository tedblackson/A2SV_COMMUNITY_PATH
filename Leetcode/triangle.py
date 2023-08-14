class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        @cache
        def dfs(row, col):
            
            if row >= len(triangle):
                return 0

            one = triangle[row][col] + dfs(row + 1, col)
            two = triangle[row][col + 1] + dfs(row + 1, col + 1)

            return min(one, two) 
        return dfs( 1, 0) + triangle[0][0]

        