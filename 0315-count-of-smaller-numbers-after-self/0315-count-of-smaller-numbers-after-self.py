class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        nums = [[num, i] for i, num in enumerate(nums)]
        ans = [0]*n
        
        
        def mergesort(start, end):
            
            if start >= end: return
            
            
            mid = start + (end - start)//2
            
            mergesort(start , mid)
            mergesort(mid + 1 , end)
            
            
            one , two = start , mid + 1
            
            
            while one <= mid and two <= end:
                
                if nums[one] <= nums[two]:
                    ans[nums[one][1]] += (two - mid - 1)
                    one += 1
                else:
                    two += 1
            
            while one <= mid:
                ans[nums[one][1]] += (two- mid - 1)
                one += 1
                    
            nums[start : end + 1] = sorted(nums[start: end + 1])
            
        mergesort(0, n - 1)
        
        return ans
            
            
            
        