class Trie:
    def __init__(self):

        self.root = [None] * 2

    def addNum(self, num):

        bitNum = bin(num).replace("0b", "")
        
        bitNum = "0" * (32 - len(bitNum)) + bitNum
        cur = self.root

        for bit in bitNum:
            bit = int(bit)
            if not cur[bit]:
                cur[bit] = [None] * 2

            cur = cur[bit]

    def max_sum(self, num1):
        bitNum = bin(num1).replace("0b","")
        bitNum = "0" * (32 - len(bitNum)) + bitNum
        cur = self.root
        res = []

        for bit in bitNum:

            if bit  == "1":
                if cur[0]:
                    cur = cur[0]
                    res.append("0")
                else:
                    cur = cur[1]
                    res.append("1")

            else:
                if cur[1]:
                    cur = cur[1]
                    res.append("1")
                else:
                    cur = cur[0]
                    res.append("0")

        num2 = int("".join(res) , 2)


        return num1 ^ num2

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:

        trie = Trie()
        maximum = 0


        for num in nums:

            trie.addNum(num)
            res = trie.max_sum(num)

            maximum = max(res, maximum)



        return maximum
