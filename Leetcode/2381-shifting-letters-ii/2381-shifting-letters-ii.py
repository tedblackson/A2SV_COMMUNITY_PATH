class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        
        prefix = [0] * (len(s) + 1)
        
        for start, end , direction in shifts:
            
            prefix[start] += 1 if direction else -1
            
            prefix[end + 1] += -1 if direction else 1
            
        prefix = list(accumulate(prefix))
        
        ans = ''
                
        for i, char in enumerate(s):
            temp = (ord(char) - ord('a') + prefix[i])%26
            ans += chr(temp + ord('a'))
        return ans
            
            
            
            
            
        