class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        
        new_releaseTimes = [releaseTimes[0]] + [0] * (len(releaseTimes)-1)
        
        for i in range(1, len(releaseTimes)):
            new_releaseTimes[i] = releaseTimes[i] - releaseTimes[i-1]
        
        # print(new_releaseTimes)
            
        ans = sorted([[i,j] for i, j in zip(new_releaseTimes, keysPressed)], key=lambda x:[x[0], x[1]])
        
        return ans[-1][1]
        
        