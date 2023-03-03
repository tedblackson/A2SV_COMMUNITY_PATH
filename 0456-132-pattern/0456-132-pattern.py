class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        
        stack = []
        maxVal = -math.inf
        
        for num in nums[::-1]:
            
            if maxVal > num:
                return True
            else:
                while stack and stack[-1] < num:
                    maxVal = stack.pop()
                    
            stack.append(num)
                
        return False