class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        
        def invert(s):
            ans = ''
            for char in s:
                ans += '0' if char == '1' else '1'
            return ans
        
        def solve(n):
            if n == 1:
                return '0'
            prev = solve(n - 1)
            return prev + '1' + invert(prev)[::-1]
        
        res = solve(n)
        return res[k - 1]