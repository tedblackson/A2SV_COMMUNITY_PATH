class Solution:
    def reverse(self, x: int) -> int:
      
        answer = 0
        num = str(x) if x > 0 else str(x)[1:]
        digits = len(num) 
 
        for i in range(digits):
            answer += int(num[i]) * pow(10, i)
        answer = answer * -1 if  x < 0 else answer
        
        return answer if pow(-2, 31) < answer < pow(2, 31) - 1 else 0
            
            