class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        
        def backtrack(arr, cur, n):
            ans.append(arr[:])
    
            if len(arr) == n:
                return
        
            for i in range(cur, len(nums)):

                arr.append(nums[i])

                backtrack(arr, i + 1 , n)
                
                arr.pop()
        backtrack([], 0, n)
        return ans
                
            
            
            