class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        reminder = defaultdict(int)
        curSum = count = 0
        reminder[0] = 1
        for ele in nums:
            curSum += ele
            count += reminder[curSum % k]
            reminder[curSum % k] += 1
        return count