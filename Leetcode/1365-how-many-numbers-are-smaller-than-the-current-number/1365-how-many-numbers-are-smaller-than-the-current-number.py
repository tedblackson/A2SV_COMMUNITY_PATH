class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        counted = dict(Counter(nums))
        location = {}
        s = sorted(nums)
        res = []
        
        for i, num in enumerate(s):
            location[num] = i
        for num in nums:
            res.append(location[num] - counted[num] + 1)
        return res
            
            
            