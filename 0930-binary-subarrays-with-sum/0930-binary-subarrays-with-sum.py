class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        sums = defaultdict(int)
        sums[0] = 1
        curSum = 0
        count = 0
        for ele in nums:
            curSum += ele
            
            count += sums[curSum - goal]
            sums[curSum] += 1
        return count