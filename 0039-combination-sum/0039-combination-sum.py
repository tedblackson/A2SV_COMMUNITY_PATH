class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        
        ans = []
        visited = set()
        
        def backtrack(cur, curSum, arr):
            
            if curSum == target:
                if tuple(sorted(arr)) not in visited:
                    visited.add(tuple(sorted(arr)))
                    ans.append(sorted(arr))
                return
            
            if curSum > target:
                return
            
            if cur >= n:
                return
            
            
            
            arr.append(candidates[cur])
            backtrack(cur + 1, curSum + candidates[cur], arr)
            arr.pop()
            
            arr.append(candidates[cur])
            backtrack(cur, curSum + candidates[cur], arr)
            arr.pop()
            
            
            backtrack(cur +1, curSum, arr)
        
        backtrack(0, 0, [])
        
        return ans