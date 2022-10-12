class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        left1 = right1 =  total= total1 = total2= 0
        max1 = max2 = maximum = 0
        visited1 = visited2 = []
        left2 = right2 = len(nums) - 1
        
        
        while(left2 >= 0 and right1 < len(nums)):
            print("max1", max1, "max2", max2 , "maximum", maximum)
            total1 += nums[right1]
            total2 += nums[left2]
            
            
            while(right1 - left1 + 1 > firstLen):
                total1 -= nums[left1]
                left1 += 1
            while(right2 - left2 + 1 > secondLen):
                total2 -= nums[right2]
                right2 -= 1
            if total2 >= max2:
                visited2 = [left2, right2] 
            if total1 >= max1:
                visited1 = [left1, right1]
            max2 = max(max2, total2)
            max1 = max(max1, total1)
            
            if(visited1[0] <= visited1[1] < visited2[0] or visited1[1] >= visited1[0] > visited2[1]):
                maximum = max(maximum, max1 + max2)
            else:
                max1 = 0 
                max2 = 0
        
            
            left2 -= 1
            right1 += 1
        return maximum

        
        