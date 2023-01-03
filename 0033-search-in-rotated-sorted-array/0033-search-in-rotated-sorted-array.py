class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        mid = left + (right - left)//2
        
        while left <= right:
            
            abnormal1 = nums[mid] <= nums[right] and target > nums[right]
            abnormal2 = nums[left] <= nums[mid] and target < nums[left]
            
            if nums[mid] == target:
                return mid
            if abnormal1 or abnormal2 :
                if target > nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
                    
                
            
            mid = left + (right - left)//2
                
        return -1
                
                
            
        