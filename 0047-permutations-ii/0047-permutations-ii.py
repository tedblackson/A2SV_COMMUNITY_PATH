class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        visited = set()
        visited2 = set()
        ans = []
        n = len(nums)
        
        
        def backtrack(arr):
            
            if len(arr) == n:
                if tuple(arr)  not in visited2:
                    ans.append(arr.copy())
                    visited2.add((tuple(arr)))
                return
            
            for i in range(len(nums)):
                
                if i not in visited:
                    arr.append(nums[i])
                    visited.add(i)
                    backtrack(arr)
                    arr.pop()
                    visited.remove(i)
                    
        backtrack([])
        
        
        
      
        return ans
    
                    