class Solution:
    def maxScore(self, nums: List[int]) -> int:
        self.ans = 0
        n = len(nums)

        base = int("1" * n, 2)
        
        
                
        @cache
        def backtrack(visited,  op):
            
            if op > n // 2:
                return 0
                
            ans = 0

            for i in range(n):
                if visited & 1 << i: continue
                
                visited |= 1 << i
                
                for j in range(i + 1, n):
                    
                    if visited & 1 << j: continue
                        
                    visited |= 1 << j
                    
                    ans =  max(op * math.gcd(nums[i], nums[j])  + backtrack(visited, op + 1), ans)
                    visited ^= 1 << j
                    
                visited ^= 1 << i
                

       
           
            
                
            return ans
        
        ans = backtrack(0, 1 )
        
        return ans
                        
                        