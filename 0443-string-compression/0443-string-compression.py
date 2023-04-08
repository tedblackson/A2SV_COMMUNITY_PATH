class Solution:
    def compress(self, chars: List[str]) -> int:
        left = right = 0
        s= ""
        chars.append(None)
        while right < len(chars):
            if chars[left] != chars[right]:
                s +=  chars[left] + str(right - left) if right -left  > 1 else chars[left]
                left = right
            right += 1
        while len(chars) != len(s):
            chars.pop()
        for i in range(len(s)):
            chars[i] = s[i]
        return len(chars)
        