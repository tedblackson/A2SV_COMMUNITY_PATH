class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        paranthesis = {")" : "("}
        
        for char in s:
            if stack and char == ')' and stack[-1] == '(':
                stack.pop()
                
                if stack and type(stack[-1]) == int:
                    stack[-1] += 1
                else:
                    stack.append(1)
            elif stack and char == ')' and type(stack[-1]) == int:
                temp = stack.pop() * 2
                stack.pop()
                if stack and type(stack[-1]) == int:
                    stack[-1] += temp
                else:
                    stack.append(temp)
            else:
                stack.append(char)
            

        return  stack.pop()
                
            
        
        
        