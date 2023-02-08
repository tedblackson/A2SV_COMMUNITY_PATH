class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        low = 0
        high = len(nums) - 1
        res = [-1, -1]

        mid = low + (high - low)//2
        while low <= high:
            if nums[mid] == target:
                res[0] = mid
                high = mid  - 1
            elif target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
            mid = low + (high - low)//2
            
        
        low = 0
        high = len(nums) - 1
        mid = low + (high - low)//2


        while low <= high:
            if nums[mid] == target:
                res[1] = mid
                low = mid + 1
            elif target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
            mid = low + (high - low)//2
            
        
        return res
        

        

        
            

                