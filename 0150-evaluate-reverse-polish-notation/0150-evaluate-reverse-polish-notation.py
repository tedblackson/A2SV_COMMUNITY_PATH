class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operation = {
            
            "+" : lambda x, y : x + y,
            "-" : lambda x, y : y - x,
            '*' : lambda x, y : x * y,
            '/' : lambda x, y :  floor(y / x) if y /x > 0 else ceil(y / x)
        }
        
        for token in tokens:
            if token in operation:
                temp = operation[token](stack.pop(), stack.pop())
                stack.append(temp)
            else:
                stack.append(int(token))
        return stack.pop()
                        