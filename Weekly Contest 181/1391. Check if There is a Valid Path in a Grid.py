#Reference: https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/discuss/547263/Python-easy-DFS

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        
        directions = {1: [(0,-1),(0,1)], #means left or right
                      2: [(-1,0),(1,0)], #means up or down
                      3: [(0,-1),(1,0)], #means left or down
                      4: [(0,1),(1,0)], #right or down
                      5: [(0,-1),(-1,0)], #left or up
                      6: [(0,1),(-1,0)]} #right or up
        
        visited = set()
        goal = (len(grid)-1, len(grid[0]) - 1)
        
        def dfs(i, j):
            visited.add((i,j))
            if (i,j) == goal: #reach final
                return True
            for d in directions[grid[i][j]]: #left and right
                ni, nj = i+d[0], j+d[1] #new location
                #-d[0] and -d[1] needed because need to know whether the next tile suits the previous.
                if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and (ni, nj) not in visited and (-d[0], -d[1]) in directions[grid[ni][nj]]:
                    if dfs(ni, nj):
                        return True
            return False
        return dfs(0,0)