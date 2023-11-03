class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = {}
        for i, num in enumerate(nums):
            if num in store:
                store[num].append(i)
            else:
                store[num] = [i]
        for num in nums:
            if (target - num) in store :
                if not ((target - num) == num and len(store[num])< 2):
                    return [store[num].pop(), store[target - num].pop()]
                
            
        
        