class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        high = max(nums)
        low = 1
        total = sum(nums)
        
        def sumEach(divisor):
            total = 0
            for ele in nums:
                total += ceil(ele/divisor)
            return total
    
        while low <= high:
            mid = low + (high - low)//2
            if sumEach(mid) <= threshold:
                high = mid - 1
                
            else:
                low = mid + 1
        return low
                
                
            



            
