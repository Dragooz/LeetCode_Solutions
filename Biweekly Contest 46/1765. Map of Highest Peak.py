#First attempt : TLE

import copy
class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        
        grid = [[0 if i==1 else 1 for i in j] for j in isWater]
        
        n = len(grid)  #row
        m = len(grid[0]) #col
        
        directions = [[0,1], [0, -1], [1, 0], [-1, 0]]
        
        def check(r, c):
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                
                if nr >= n or nc >= m or nr<0 or nc<0: #uncomparable
                    continue
                else: #compare
                    new_val = grid[r][c] + 1
                    if abs(grid[nr][nc] - new_val) >= 2:
                        return False
            return True
        
        grid_prev = None
        while grid_prev != grid:
            grid_prev = copy.deepcopy(grid)
            for r in range(n):
                for c in range(m):
                    if grid[r][c] != 0 and check(r, c) :
                        grid[r][c] += 1
                        
            # print(grid_prev)
            # print(grid)
                        
        return grid
            
#Second attempt:
#Reference: https://leetcode.com/problems/map-of-highest-peak/discuss/1074551/PythonJava-BFS-from-cell-with-lowest-height-Clean-and-Concise by hiepit

import copy
class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        #BFS
        n = len(isWater)  #row
        m = len(isWater[0]) #col
        
        grid = [[-1]*m for _ in isWater]
        bfs = []
        
        directions = [[0,1], [0, -1], [1, 0], [-1, 0]]

        for i in range(n):
            for j in range(m):
                if isWater[i][j] == 1:
                    grid[i][j] = 0
                    bfs.append([i,j])
                    
        while bfs:         
            
            r, c = bfs.pop(0)
            
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                
                if nr >= n or nc >= m or nr<0 or nc<0 or grid[nr][nc] != -1: #uncomparable
                    continue
                else: #compare
                    grid[nr][nc] = grid[r][c] +1
                    bfs.append([nr,nc])   
                        
        return grid
            