class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        visited = set()
        def backtrack(arr, cur):
            if len(arr) > 1:
                if tuple(arr) not in visited:
                    ans.append(arr[:])
                    visited.add(tuple(arr))
            
        

            
            for i in range(cur , n):
                if arr and arr[-1] > nums[i]:
                    continue
                arr.append(nums[i])
                
                backtrack(arr, i + 1)
                arr.pop()
        backtrack([], 0)
        return ans          
            