class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = Counter(nums)
        ans = 0
        for value in count.values():
            if value >= 2:
                ans += comb(value, 2)
        return ans