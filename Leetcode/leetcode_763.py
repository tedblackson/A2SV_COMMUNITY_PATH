class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        size = right= 0
        last = {}
        res = []
        
        for left, char in enumerate(s):
            last[char]  = left
        
        for left , char in enumerate(s):
            size += 1
            right = max(right, last[char])
            if left == right:
                res.append(size)
                size = 0
        return res