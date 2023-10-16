class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        n = len(s)
        stack = []
        for i in range(n):
            if not stack or stack[-1][0] != s[i]:
                stack.append((s[i], 1))
            else:
                stack.append((s[i], stack[-1][1] + 1))
            
            
            if stack[-1][1] == k:
                
                for _ in range(k):
                    stack.pop()
        
            
        stack = [ char[0] for char in stack]
        ans = "".join(stack)
        
        return ans
            
                
                