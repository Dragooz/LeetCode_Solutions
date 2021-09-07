class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        
        m = len(grid)
        
        n = len(grid[0])
        
        def dp(a, row):
            
            if 0>a or a>n-1 : return -1 
            
            if row == m: return a
            
            if grid[row][a] == 1: #only see right
                if a == n-1: return -1
                if grid[row][a+1] == grid[row][a]:
                    return dp(a+1, row+1)
                else:
                    return -1
            else: #only see left
                if a == 0: return -1
                if grid[row][a-1] == grid[row][a]:
                    return dp(a-1, row+1)
                else:
                    return -1
        
        ans = []
        for i in range(n):
            ans.append(dp(i, 0))
            
        return ans