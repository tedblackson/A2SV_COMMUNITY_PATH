class Solution:
    def isPalindrome(self, x: int) -> bool:
        string= str(x)
        string_2 = string[::-1]
        print(string_2)
        if string==string_2:
            return True
        return False