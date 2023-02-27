class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        
        stack = []
        count = Counter(s)
        used = set()
        
        for char in s:
            
            if char not in used:
                while stack and stack[-1] >= char and count[stack[-1]] > 0 and char not in used:
                    used.remove(stack.pop())
                    
                
                stack.append(char)
                used.add(char)
            count[char] -= 1
        
        return ''.join(stack)
        