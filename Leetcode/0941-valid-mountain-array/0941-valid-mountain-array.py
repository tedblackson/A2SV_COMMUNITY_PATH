class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:

        maxx = max(arr)

        for i in range(len(arr)):

            if arr[i] == maxx:

                side1 = arr[:i] == sorted(arr[:i]) and len(arr[:i]) == len(set(arr[:i])) != 0
                side2 = arr[i:] == sorted(arr[i:], reverse = True) and len(arr[i:]) == len(set(arr[i:])) != 1

                return side1 and side2 == True
                

        