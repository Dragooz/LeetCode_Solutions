#First Attempt: TLE

from functools import lru_cache

class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        
        length = len(rides)
        rides.sort()
        
        @lru_cache(None)
        def dp(index, profit):
            
            f_start, f_end, f_tip = rides[index]
            
            new_profit = profit + (f_end - f_start +  f_tip)
            
            if f_end >= n or index+1 == length:
                return new_profit
            
            max_prof = new_profit
            for i in range(index+1, length):
                start, _, _ = rides[i]
                if start >= f_end: #can proceed
                    max_prof = max(max_prof, dp(i, new_profit))
                
            return max_prof
        
        ans = 0
        for i in range(length):
            ans = max(ans, dp(i, 0))
            
        return ans

#Second Attempt: Reference: https://leetcode.com/problems/maximum-earnings-from-taxi/discuss/1470885/Python-dp-with-binary-search-explained

class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        
        length = len(rides)
        rides.sort()
        S = [i[0] for i in rides]
        
        dp = [0]*(length+1)
        # print(rides)
        # print(S)
        for i in range(length-1, -1, -1):
            temp = bisect.bisect_left(S, rides[i][1])
            # print(temp)
            dp[i] = max(dp[i+1], rides[i][2] + rides[i][1] - rides[i][0] + dp[temp])
            # print(dp)
        
        return dp[0]