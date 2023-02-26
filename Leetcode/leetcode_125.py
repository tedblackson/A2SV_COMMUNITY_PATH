class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        newString = ''
        for st in s:
            if st.isalnum():
                newString += st
        
        return newString == newString[::-1]
        