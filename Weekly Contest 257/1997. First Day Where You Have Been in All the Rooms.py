#Reference: https://leetcode.com/problems/first-day-where-you-have-been-in-all-the-rooms/discuss/1445225/Python-short-dp-explained

class Solution:
    def firstDayBeenInAllRooms(self, nextVisit: List[int]) -> int:
        
        n = len(nextVisit)
        mod = 10**9 + 7
        
        dp = [0] * n
        
        for i in range(1, n):
            '''
            1. Steps to reach room i-1 for the first time, which is steps[i-1]
            2. 1 step to go to nextVisit[i-1]
            3. Steps to reach room i-1 for the second time, which is steps[i-1] - steps[nextVisit[i-1]], since this time we start from room                  nextVisit[i-1] instead of room 0
            4. 1 step to finally move to room i
            
            '''
            dp[i] = (2*dp[i-1] - dp[nextVisit[i-1]] + 2) % mod
    
    
        return dp[-1]