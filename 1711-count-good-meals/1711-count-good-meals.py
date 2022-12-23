class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        res = 0
        
        count = defaultdict(lambda: 0)

        for taste in deliciousness:
            for value in range(22):
                res += count[2**value - taste]
            count[taste] += 1
        return res%(10**9 + 7)