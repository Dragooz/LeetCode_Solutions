#Reference: https://leetcode.com/problems/maximum-non-negative-product-in-a-matrix/discuss/855131/Python3-top-down-dp

class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        mod = 10**9 + 7
        
        @lru_cache(None)
        def dp(i, j):
            
            if i == m-1 and j == n-1: #reach
                return grid[i][j], grid[i][j]
            
            if i == m or j == n:
                return -inf, inf #max, min
            
            mx1, mn1 = dp(i+1, j)
            mx2, mn2 = dp(i, j+1)
            
            mx, mn = max(mx1, mx2) * grid[i][j], min(mn1, mn2) * grid[i][j]
            
            return (mx, mn) if grid[i][j] > 0 else (mn, mx)
        
        mx, _ = dp(0, 0)
        
        return -1 if mx < 0 else mx%mod
            