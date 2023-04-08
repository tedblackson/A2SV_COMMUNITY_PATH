class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        ans = defaultdict(int)
        _max = 0
        n = len(nums)
        
        def backtrack(arr, cur):
            nonlocal _max
            temp = 0
            for ele in arr:
                temp |= ele
                
            if temp > _max:
                _max = temp
                
            ans[temp] += 1
            

            
            for i in range(cur, len(nums)):
                arr.append(nums[i])
                backtrack(arr, i + 1)
                arr.pop()
        backtrack([], 0)
        
        return ans[_max]