class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        counted = Counter(nums)
        
        for key, value in counted.items():
            if value > len(nums)//2:
                return key