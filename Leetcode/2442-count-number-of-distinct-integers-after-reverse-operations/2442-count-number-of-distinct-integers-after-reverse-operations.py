class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        new = []
        
        for num in nums:
            temp = str(num)
            new.append(int(temp[::-1]))
        nums += new
        return len(set(nums))