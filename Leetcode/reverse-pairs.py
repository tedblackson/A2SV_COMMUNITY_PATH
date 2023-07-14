class Solution:
    def reversePairs(self, nums: List[int]) -> int:

        def mergeSort(low, high):

            if low >= high:
                return 0
            
            mid = low + (high - low)//2

            count = mergeSort(low, mid) + mergeSort(mid + 1, high)

            one, two = low,  mid + 1

            while one <= mid and two <= high:
                if nums[one] > 2 * nums[two]:
                    count += mid - one + 1
                    two +=1
                else:
                    one += 1
            nums[low : high + 1] =  self.merge(nums[low: mid + 1], nums[mid + 1: high + 1])[:]
            return count
            
        return mergeSort(0, len(nums) - 1)

    def merge(self, left , right):

        one = two = 0
        merged = []

        while one < len(left) and two < len(right):
            
            if left[one] <= right[two]:
                merged.append(left[one])
                one += 1
            else:
                merged.append(right[two])
                two += 1
        
        merged.extend(left[one:])
        merged.extend(right[two:])
        return merged



    

    
        