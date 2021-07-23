#Reference:
#https://leetcode.com/problems/minimum-path-sum/discuss/23532/Python-Solution-with-Detailed-Explanation by gabbu

import functools
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        #down right each, save min possible solution for each step
        
        m, n = len(grid), len(grid[0])
        cost = [[0]*n for _ in range(m)]
        cost[0][0] = grid[0][0]
        
        for i in range(1,n):
            cost[0][i] = grid[0][i] + cost[0][i-1]
        for j in range(1, m):
            cost[j][0] = grid[j][0] + cost[j-1][0]
            
        for i in range(1,m):
            for j in range(1, n):
                cost[i][j] = min(cost[i-1][j], cost[i][j-1]) + grid[i][j] #come from above or left
        return cost[m-1][n-1]