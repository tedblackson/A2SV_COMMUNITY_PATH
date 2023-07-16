class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        
        ans = [0] * len(nums)
        nums = [(num, i) for i, num in enumerate(nums)]
        
        
        def mergeSort(start, end):
            
            if start >= end:
                
                return [nums[start]]
            
            
            mid = start + (end - start)//2
            
            leftHalf = mergeSort(start, mid) 
            rightHalf = mergeSort(mid + 1, end)
            
            one , two = start , mid + 1
            
            
            while one <= mid and two <= end:
                
                if nums[one][0] <= nums[two][0]:
                    
                    ans[nums[one][1]] += two - mid - 1
                    one += 1
                else:
                    two += 1
            while one <= mid:
                ans[nums[one][1]] += two - mid -1
                one += 1
            
            
            nums[start : end + 1] = sorted(nums[start:end + 1])
            
        mergeSort(0, len(nums) - 1)
        
        return ans            
        