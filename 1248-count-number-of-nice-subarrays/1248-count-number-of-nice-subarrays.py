class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        for i in range(len(nums)):
            nums[i] %= 2
        total = defaultdict(int)
        curSum = count = 0
        total[0] = 1
        for ele in nums:
            curSum += ele
            count += total[curSum - k]
            total[curSum] += 1
        return count
        
        
                