class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        total = sum(list(filter(lambda x : not x % 2, nums)))
        ans = []
        for val , index in queries:
            if not nums[index] % 2 :
                total -= nums[index]
            if not (nums[index] + val) % 2:
                total += (nums[index] + val)
            nums[index] = nums[index] + val
            ans.append(total)
        return ans
            
        
        
        
        