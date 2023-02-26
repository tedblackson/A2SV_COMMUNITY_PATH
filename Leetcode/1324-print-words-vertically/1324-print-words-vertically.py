class Solution:
    def printVertically(self, s: str) -> List[str]:
        
        s = s.split()
        ans = []
        maxCol = len(max(s, key = lambda x : len(x)))
        
        for col in range(maxCol):
            temp = ''
            for row in range(len(s)):
                if col < len(s[row]):
                    temp += s[row][col]
                else:
                    temp += ' '
            ans.append(temp.rstrip())
        return ans
            