class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        ans = []
    
        def backtrack( cur, arr):
            
            if len(arr) == k:
                ans.append(arr[:])
                return
            
            for candidate in range(cur, n + 1):
                arr.append(candidate)
                backtrack(candidate + 1 , arr)
                arr.pop()
            
        backtrack(1 ,[])
            
                
                
        return ans
            
                
            
            
            
            