class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        stack = []
        
        for ele in path:
            if ele != '' and ele != '..' and ele != '.':
                stack.append(ele)
            elif ele == '..':
                if stack:
                    stack.pop() 
        ans = '/'.join(stack)
        ans = '/' + ans
        return ans
            