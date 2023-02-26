class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        
        product = 1
        start = count = 0
        for end in range(len(nums)):
            product *= nums[end]
            while start <= end and product >= k:
                product /= nums[start]
                start += 1
            count += end - start + 1

        return count
                