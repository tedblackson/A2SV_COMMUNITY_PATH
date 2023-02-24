class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        total = defaultdict(int)
        total[0] = 1
        curSum = count = 0
        for ele in nums:
            curSum += ele
            count += total[curSum - k]
            total[curSum] += 1
        return count
        
        