class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        merge = [(ages[i], scores[i]) for i in range(len(scores))]
        merge.sort()
        
        
        
        dp = [score for _ , score in merge]

        for i in range(len(scores)):
          _max = 0
         
          for j in range(i):
            if merge[j][1]<= merge[i][1] :
              _max = max(_max, dp[j])
          dp[i] += _max


        return max(dp)

