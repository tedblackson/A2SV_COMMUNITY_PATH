class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        ans = 0
        for col in range(len(strs[0])):
            
            delete = False
            prev = strs[0][col]
            for row in range(len(strs)):
                if prev > strs[row][col]:
                    delete = True
                prev = strs[row][col]
            if delete:
                ans += 1
        return ans
                
                
        