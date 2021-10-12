#Reference: https://leetcode.com/problems/minimum-number-of-days-to-disconnect-island/discuss/819303/Python-you-need-at-most-2-days

class Solution:
    
    def recur_island(self, grid, i, j, m, n):
        if grid[i][j] == 0:
            return
        
        grid[i][j] = 0
        
        if i+1< m:
            self.recur_island(grid, i+1, j, m, n)
        if i-1 >= 0:
            self.recur_island(grid, i-1, j, m, n)
        if j+1 < n:
            self.recur_island(grid, i, j+1, m, n)
        if j-1 >=0:
            self.recur_island(grid, i, j-1, m, n)
    
    def island(self, grid, m, n):
        num_island = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    num_island +=1
                    self.recur_island(grid, i, j, m, n)
                    
        return num_island
    
    def minDays(self, grid: List[List[int]]) -> int:
        #if number of island is 1, then it's connected, else its not.
        m, n = len(grid), len(grid[0])
        
        #day0
        grid_2 = copy.deepcopy(grid)
        if self.island(grid_2, m, n) != 1:
            return 0
        
        #day1
        for i in range(m):
            for j in range(n):
                grid_3 = copy.deepcopy(grid)
                grid_3[i][j] = 0
                
                if self.island(grid_3, m, n) != 1:
                    return 1
        
        #day2 - the maximum day need to make them unconnect.
        return 2
        
            
            
        