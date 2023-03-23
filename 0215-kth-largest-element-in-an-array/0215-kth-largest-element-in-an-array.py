class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-num for num in nums]
        
        heapify(nums)
        
        while k > 1:
            heappop(nums)
            k -= 1
        return -1 * heappop(nums)
        