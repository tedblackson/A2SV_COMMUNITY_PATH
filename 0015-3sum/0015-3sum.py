class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # Sort the array
        nums.sort()
    
        # Initialize a list to store the triplets
        triplets = []
    
        # Iterate over the array
        for i in range(len(nums) - 2):
            # If the current element is greater than 0, we can stop
            # because the triplets must sum to 0
            if nums[i] > 0:
                break
            # If the current element is the same as the previous element,
            # we can skip it to avoid duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue
    
            # Initialize pointers for the two remaining elements
            j = i + 1
            k = len(nums) - 1
    
            # Find the two remaining elements that sum to -nums[i]
            while j < k:
                if nums[j] + nums[k] == -nums[i]:
                    triplets.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    # Skip duplicates
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                elif nums[j] + nums[k] < -nums[i]:
                    j += 1
                else:
                    k -= 1
    
        return triplets
            