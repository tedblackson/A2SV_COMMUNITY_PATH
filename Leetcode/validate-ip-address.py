class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        dotCount = queryIP.count(".")
        colonCount = queryIP.count(":")
        n = len(queryIP)
        


        if not queryIP or not (dotCount == 3 or colonCount == 7) :
            return "Neither"
        
        end = queryIP[-1]

        
        
        prev = 0
        if dotCount == 3:
            for i in range(n + 1):
                
                if i == n  or queryIP[i] == "."  :

                    seg = queryIP[prev: i]
                    intSeg = int(seg) if seg else float('inf')
                    _len = len(seg)
                    if _len == 0 or _len > 3 or not(len(str(int(seg))) == _len) or not (0 <= intSeg <= 255) :
                        return "Neither"
                    prev = i + 1
                    


                elif i < n and not (48 <= ord(queryIP[i]) <= 57 ):
                    return "Neither"


                
            return "IPv4"
        elif colonCount == 7:


            for i in range(n + 1):
                if i < n:
                    char = ord(queryIP[i])
                num = 48 <= char <= 57
                lower = 97 <= char <= 102
                upper = 65 <= char <= 70
                if i == n or queryIP[i] == ":" :
                    seg = queryIP[prev: i]
                    _len = len(seg)
                    if _len == 0 or _len > 4:
                        
                        return "Neither"
                    prev = i + 1
                    

                elif i < n and  not ( num or lower or upper):
                    return "Neither"
                
            return "IPv6"
        else:
            return "Neither"
            
            


        



        