class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        n = len(players)
        idx = 0
        ans =0
        for i in range(len(trainers)):
            if idx < n and trainers[i] >= players[idx]:
                ans += 1
                idx += 1
        return ans
            
            
            