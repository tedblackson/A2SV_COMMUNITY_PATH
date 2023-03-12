class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
       
        
        ans = []
        
        def backtrack(arr, cur):
            ans.append(arr[:])
    
            if len(arr) == len(nums):
                return
        
            for i in range(cur, len(nums)):

                arr.append(nums[i])

                backtrack(arr, i + 1 )
                
                arr.pop()
        backtrack([], 0)
        return ans            