class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count1 = dict(Counter(s))
        count2 = dict(Counter(t))
        

        for key, value in count2.items():
            if count2[key] != count1.get(key):
                return key


