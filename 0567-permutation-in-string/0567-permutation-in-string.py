class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        sorted1 = sorted(s1)
        start = 0
        
        for end in range(len(s1) ,len(s2) + 1):
            if sorted(s2[start: end]) == sorted1:
                return True
            start += 1
            
        return False