class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        
        
        hashV = 0
        n = len(s)
        
        left = 0
        p = 1
        for i in range(k ):
            hashV += (ord(s[i]) - ord('`')) * p
            p *= power
        p //= power
        
        if hashV % modulo == hashValue:
            return s[left: k]
        
        for right in range(k , n):
            
            new = ord(s[right]) - ord("`")  
            first = ord(s[left]) - ord("`") 
         
            hashV = ((hashV - first)//power) + new * p
            left += 1
            
            if hashV % modulo == hashValue :
                return s[left:right + 1]
        
        

            