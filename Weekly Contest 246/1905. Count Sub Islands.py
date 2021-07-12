'''
References:
https://leetcode.com/problems/count-sub-islands/discuss/1284319/JavaC%2B%2BPython-DFS-Solution by lee215
https://leetcode.com/problems/number-of-islands/
'''

#200 numbers of island.
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        m, n = len(grid), len(grid[0])
        four_direction = [[0,1],[1,0],[-1,0],[0,-1]] #right, down, up, left
        
        def dfs(i, j):
            #break and return 0 if one of these 3 condition = False
            #1. out of boundaries m
            #2. out of boundaries n
            #3. grid is visited.
            if not(0<=i<m and 0<=j<n and grid[i][j]=='1'):
                return 0
            
            #visited
            grid[i][j] = '0'
            
            #create 4 directions from the points.
            for row, col in four_direction:
                dfs(i+row, j+col)
            
            return 1
        
        ans = 0
        for i in range(m):
            for j in range(n):
                #only run if its land
                if grid[i][j] == '1':
                    ans += dfs(i, j)
        
        return ans
            
            
            
#1905. Count Sub Islands
class Solution(object):
    def countSubIslands(self, grid1, grid2):
        """
        :type grid1: List[List[int]]
        :type grid2: List[List[int]]
        :rtype: int
        """
        
        m, n = len(grid1), len(grid1[0])
        four_direction = [[0,1],[1,0],[-1,0],[0,-1]] #right, down, up, left
        
        def dfs(i, j):
            #break and return 1 if one of these 3 condition = False (return 1 is to indicate that its a part of the island)
            #that can be used to comapred with grid1 (master)
            #1. out of boundaries m
            #2. out of boundaries n
            #3. grid is visited.
            if not(0<=i<m and 0<=j<n and grid2[i][j]==1):
                return 1
            
            #visited
            grid2[i][j] = 0
            to_compare = grid1[i][j] #to know whether grid2 is subset.
            
            #create 4 directions from the points.
            for row, col in four_direction:
                #AND operator, to know whether the linked 1's in grid 2 match with grid 1
                to_compare = to_compare & dfs(i+row, j+col)
            
            return to_compare
        
        ans = 0
        for i in range(m):
            for j in range(n):
                #only run if its land
                if grid2[i][j] == 1:
                    ans += dfs(i, j)
        
        return ans
    

            