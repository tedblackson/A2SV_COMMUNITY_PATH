class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        prefix = [0] * (len(nums) + 1)
        nums.sort(reverse = True)
        
        for start, end in requests:
            
            prefix[start] += 1
            prefix[end + 1] -= 1
        
        prefix = list(accumulate(prefix))
        
        prefix.sort(reverse = True)
        
        ans = 0
        
        for num, freq in zip(nums, prefix):
            ans += num * freq
        
        return ans % (pow(10, 9) + 7)
        
        
        
        
        
        
        
        
        
        
        
        
        