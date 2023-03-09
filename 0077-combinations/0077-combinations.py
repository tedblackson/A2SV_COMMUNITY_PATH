class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        ans = []
        
        def backtrack(arr, curr):
            
            if len(arr) == k:
                ans.append(arr.copy())
                return
            for i in range(curr + 1 , n + 1):
                arr.append(i)
                backtrack(arr, i)
                arr.pop()
                
        backtrack([], 0)
                
        return ans
            
                
            
            
            
            