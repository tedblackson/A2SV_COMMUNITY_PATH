class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        ans = []
        visited = set()
        
        def backtrack(arr, cur):
            
            if tuple(sorted(arr)) not in visited:
                
                ans.append(arr[:])
                visited.add(tuple(sorted(arr)))
            
            if len(arr) == len(nums):
                return
#             1 2
#             2 1
                
            for i in range(cur, len(nums)):
                arr.append(nums[i])
                backtrack(arr, i + 1)
                arr.pop()
        backtrack([], 0)
        return ans
            
                