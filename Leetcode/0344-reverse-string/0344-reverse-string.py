class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) -1
        
        def reverse(left, right):
            
            if left > right:
                return
            else:
                s[left], s[right] = s[right] , s[left]
                reverse(left +1, right -1)
        reverse(left, right)