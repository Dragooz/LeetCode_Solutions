import copy

class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        
        
        m = len(land)
        n = len(land[0])
        
        row = 0
        col = 0
        
        ans = []
        
        while row < m and col < n:
            
            if 1 not in land[row]:
                row+=1
                col=0
                continue

            if land[row][col] == 1:
                new_r = copy.copy(row)
                new_c = copy.copy(col)

                while new_r+1 < m and land[new_r+1][new_c] == 1:
                    new_r +=1

                while new_c+1 < n and land[new_r][new_c+1] == 1:
                    new_c +=1
                
                ans.append([row,col,new_r,new_c])
                
                for i in range(row, new_r+1):
                    for j in range(col, new_c+1):
                        land[i][j] = 0
                        
                col = copy.copy(new_c)
                
                
            if col == n -1:
                row +=1
                col = 0
            else:
                col +=1
                
        return ans

#Reference BFS https://leetcode.com/problems/find-all-groups-of-farmland/discuss/1444115/Python3-dfs

import copy

class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        
        m = len(land)
        n = len(land[0])
        
        ans =[]
        for i in range(m):
            for j in range(n):
                
                if land[i][j]:
                    
                    min_i, min_j = i, j
                    max_i, max_j = i, j
                    
                    stack = [(i, j)]
                    land[i][j] = 0
                    
                    while stack:
                        i, j = stack.pop()
                        
                        for ii, jj in (i-1, j), (i, j-1), (i, j+1), (i+1, j):
                            if 0<=ii<m and 0<=jj<n and land[ii][jj]:
                                stack.append((ii,jj))
                                land[ii][jj] = 0
                                max_i = max(max_i, ii)
                                max_j = max(max_j, jj)
                                
                    ans.append([min_i, min_j, max_i, max_j])
                    
        return ans



