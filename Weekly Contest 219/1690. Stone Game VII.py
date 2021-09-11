#Reference: https://leetcode.com/problems/stone-game-vii/discuss/970268/C%2B%2BPython-O(n-*-n)

from functools import lru_cache

class Solution:
    def stoneGameVII(self, s: List[int]) -> int:
        dp = [[0] * len(s) for _ in range(len(s))]
        p_sum = [0] + list(accumulate(s)) #two index diff here = the sum between
        
        @lru_cache(None)
        def dfs(i , j):
            if i == j: #no diff
                return 0
            if dp[i][j] == 0: #haven't seen
                sum_ = p_sum[j + 1] - p_sum[i] #the sum of particular range
                dp[i][j] = max(sum_ - s[i] - dfs(i + 1, j), sum_ - s[j] - dfs(i, j - 1)) #get the max diff
            return dp[i][j]
        res = dfs(0, len(s) - 1)
        return res
        