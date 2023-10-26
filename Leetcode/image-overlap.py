class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)

        def inBound(row, col):
             return 0 <= row < n and 0 <= col < n
        
        def countOverlap(r, c):
            cnt = 0

            for row in range(n):
                for col in range(n):
                    _row = row + r
                    _col = col + c

                    if inBound(_row, _col):
                        cnt += img1[_row][_col] == img2[row][col] == 1
            return cnt
        
        ans =0
        for r in range(-n + 1, n):
            for c in range(-n + 1, n):
                ans = max(ans, countOverlap(r, c))
        return ans



        