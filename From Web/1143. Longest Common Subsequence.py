#Reference:
#https://leetcode.com/problems/longest-common-subsequence/discuss/436719/Python-very-detailed-solution-with-explanation-and-walkthrough-step-by-step. by hxuanhung

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        m = len(text1)
        n = len(text2)
        
        memo = [[0 for _ in range(n + 1)] for _ in range(m + 1)] #create a table

        for row in range(1, m + 1):
            for col in range(1, n + 1):
                if text1[row - 1] == text2[col - 1]: #
                    memo[row][col] = 1 + memo[row - 1][col - 1] #increment by 1
                else:
                    memo[row][col] = max(memo[row][col - 1], memo[row - 1][col]) #inherit

        return memo[m][n]