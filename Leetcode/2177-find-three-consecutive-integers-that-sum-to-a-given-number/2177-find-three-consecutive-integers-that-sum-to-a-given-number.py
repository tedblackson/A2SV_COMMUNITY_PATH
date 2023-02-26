class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        
        if not num % 3:
            consec = num//3 + 1
            return [consec - 2, consec - 1, consec]
        else:
            return []