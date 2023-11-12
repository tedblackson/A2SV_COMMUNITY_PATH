class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n = len(s)
        m = len(p)

        @cache
        def dp(sidx, pidx ):
            
            
            if sidx >= n and pidx >= m:
                return True
            
            if pidx >= m:
                return False
            
            res = False
            
            if pidx + 1 < m and p[pidx + 1] == "*":
                
                res = res or dp(sidx, pidx + 2)
                if sidx < n and (p[pidx] == s[sidx] or p[pidx] =="."):
                    res = res or dp(sidx +1, pidx)
            if sidx < n and (p[pidx] == s[sidx] or p[pidx] == "."):
                
                res = res or dp(sidx + 1, pidx + 1)
            
            return res
            

            

    
        
        ans = dp(0, 0)
        return ans


            
