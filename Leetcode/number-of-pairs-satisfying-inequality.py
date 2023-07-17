class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        n = len(nums1) 
        nums = [num1 - num2 for num1, num2 in zip(nums1, nums2)]
        
        
        
        def mergeSort(low, high):

            if low >= high:
                return 0
            
            mid = low + (high - low)//2

            count = mergeSort(low, mid) + mergeSort(mid + 1, high)

            one, two = low,  mid + 1

            while one <= mid and two <= high:
                if nums[one] <= nums[two] + diff:
                    count += mid - one + 1
                    two +=1
                else:
                    one += 1
            nums[low : high + 1] =  sorted(nums[low: high + 1], reverse = True)
            return count
            
        return mergeSort(0, len(nums) - 1)
               
            

            
            
            
                    
            
