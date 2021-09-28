class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        
        n = len(scores)
        players = [[a, b]for a,b in zip(ages, scores)]
        
        players.sort(reverse=True)
        # print(players)
        
        dp = [0] * n
        
        for i in range(n):
            score = players[i][1]
            dp[i] = score
            
            for j in range(i):
                s = players[j][1]
                if s >= score: #age of j is >= i, next is to check whether the old score >= new score, if yes then its valid.
                    dp[i] = max(dp[i], dp[j] + score)
                
        return max(dp)
                