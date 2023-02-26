class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        
        winners = [match[0] for match in matches]
        losers = [match[1] for match in matches]
        players = set(winners + losers)
        losersCount = dict(Counter(losers))
        
        wonAll = []
        lostOne = []
        for player in players:
            if player not in losersCount:
                wonAll.append(player)
            elif losersCount.get(player) == 1:
                lostOne.append(player)
        return [sorted(wonAll), sorted(lostOne)]
                
            
            
            
        
        