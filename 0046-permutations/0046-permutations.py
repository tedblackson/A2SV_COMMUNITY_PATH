class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        visited = set()
        n = len(nums)
        ans = []
        def backtrack(arr):
            
            if len(arr) == n:
                ans.append(arr.copy())
                return
            
            for ele in nums:
                if ele not in visited:
                    arr.append(ele)
                    visited.add(ele)
                    backtrack(arr)
                    visited.remove(ele)
                    arr.pop()
        backtrack([])
    
        return ans
            
            
            
            
            
            