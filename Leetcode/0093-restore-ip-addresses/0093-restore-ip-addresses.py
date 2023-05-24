class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = set()
        def backtrack(start, cuts, address):
            
            if cuts == 4 and start >= len(s):
                ip_address = ".".join(address)
                if len(s) + 3 == len(ip_address):
                    ans.add(ip_address)
                
            
            for step in range(1, 4):
                cur = s[start : start + step]
                if cur:
                    cur_int = int(cur) 
                if cur and len(str(cur_int)) == len(cur) and 0 <= cur_int <= 255:
                    address.append(cur)
                    backtrack(start + step , cuts + 1, address)
                    address.pop()
             
                    
        backtrack(0, 0, [])
        return list(ans)