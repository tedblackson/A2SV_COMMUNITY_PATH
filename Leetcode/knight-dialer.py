class Solution:
    def knightDialer(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        
        directions = [[2, 1], [2, -1],[1, 2], [-1, 2], [-2, 1], [-2, -1], [-1, -2], [1, -2]]
        
        def inBound(row, col):
            return 0 <= row < 4 and 0 <= col < 3 and (row, col) != (3, 0) and (row, col) != (3, 2)
        
        @cache
        def dp(row, col , _len):
            if _len == n:
                return 1
            cnt = 0
            for r, c in directions:
                _row = row + r
                _col = col + c
                
                if inBound(_row, _col):
                    cnt += (dp(_row, _col, _len + 1))% MOD
                    cnt %= MOD
            return cnt
        
        
        
        ans = 0
        for row in range(4):
            for col in range(3):
                if inBound(row, col):
                    ans += dp(row, col, 1)
                    ans %= MOD
        
        
        return ans
                
                    