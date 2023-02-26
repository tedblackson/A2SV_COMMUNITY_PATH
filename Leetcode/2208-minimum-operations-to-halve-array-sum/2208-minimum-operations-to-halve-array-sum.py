class Solution:
    def halveArray(self, nums: List[int]) -> int:
        total = sum(nums)
        half = total/2
        operations = 0
        nums = [-1 * num for num in nums]
        heapify(nums)
        
        while total > half:
            maxVal = heappop(nums)
            maxVal /= 2
            heappush(nums, maxVal)
            total -= -1 * maxVal
            operations += 1
        return operations
            
            
            
            
        
        