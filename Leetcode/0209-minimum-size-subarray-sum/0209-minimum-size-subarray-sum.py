class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        shortest = math.inf
        total = 0
        left = 0
        
        for right in range(len(nums)):
            total += nums[right]
            while total >= target:
                shortest = min(shortest, right - left + 1) if total >= target else shortest
                total -= nums[left]
                left += 1
        return shortest if shortest != math.inf else 0
            
            