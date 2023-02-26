class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        expected = [i for i in range(1,len(arr) + 1)] 
        
        if arr == expected:
            return []
        
        left , right = 0, len(arr) - 1
        res = []
        
        while left <= right:
            maximum = (0, 0)
            for i, ele in enumerate(arr[0: right + 1]):
                if ele > maximum[0]:
                    maximum = (ele, i)
            if maximum[1] == left:
                arr = list(reversed(arr[left: right + 1])) + arr[right + 1: len(arr)]
                res.append(right + 1)
                right -= 1
            elif maximum[1] == right:
                right -= 1
                continue
            else: 
                res.append(maximum[1] + 1)
                arr = list(reversed(arr[left: maximum[1] + 1])) + arr[maximum[1] + 1: len(arr)] 
        return res
                
                
                
                
            
