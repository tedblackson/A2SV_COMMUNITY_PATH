class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        right = 0
        left = 0
        while right < len(popped):
            if (len(stack) == 0 or popped[right] != stack[-1] ):
                if(left >= len(pushed)):
                    break
                stack.append(pushed[left])

                left += 1
            
            while ( len(stack) > 0 and stack[-1] == popped[right]):
                stack.pop()
                right += 1
        
        return True if len(stack) == 0 else False
                