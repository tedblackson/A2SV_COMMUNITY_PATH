class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        nums = [-1 * num for num in nums]
        heapify(nums)
        ans = 0
        for _ in range(k):
            ans = heappop(nums)
        return -1 * ans
            
        