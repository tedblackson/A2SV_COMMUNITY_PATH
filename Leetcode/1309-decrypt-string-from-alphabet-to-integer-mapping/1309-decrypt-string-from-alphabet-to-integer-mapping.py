class Solution:
    def freqAlphabets(self, s: str) -> str:
        start = 97
        end = 123
        map = {}
        newS = ''

        for i in range(1, 27):
            map[str(i)] = chr(start)
            start += 1
        
        ctr = len(s) -1
        while ctr >= 0:
            if s[ctr] == '#':
                newS += map[ s[ctr - 2] + s[ctr -1]]
                ctr -=3
            else:
                newS += map[s[ctr]]
                ctr -= 1
        return newS[::-1]


    
        
