class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = {}
        tempStack = []
        ans = []
        
        for i in range(len(nums2)):
            result[nums2[i]] = -1
            while(len(tempStack) > 0 and tempStack[-1] < nums2[i]):
                result[tempStack.pop()] = nums2[i]

            tempStack.append(nums2[i])
        print(result)
        
        
        for i in range(len(nums1)):
            ans.append(result[nums1[i]])
            
        return ans
            