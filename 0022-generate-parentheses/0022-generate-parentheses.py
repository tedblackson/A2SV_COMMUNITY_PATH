class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        
        def backtrack(left, right, cur):
            if left == right == 0:
                ans.append(cur)
                
            if left > 0:
                backtrack(left - 1, right, cur + '(')
            
            if right > left and right > 0:
                backtrack(left, right - 1, cur + ')')
            
        backtrack(n, n, '')
        return ans