#reference:
#https://leetcode.com/problems/largest-magic-square/discuss/1267632/C%2B%2BPython-Prefix-Sum-by-rows-and-columns-Clean-and-Concise-O(M3-*-N) by hiepit

class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        
        #main idea: slide through the grid with largest. 
        #use prefix sum
        m = len(grid)
        n = len(grid[0])

        mcl = min(m, n)
        
        pre_sum_row = [[0] * (n+1) for _ in range(m)]
        pre_sum_col = [[0] * (m+1) for _ in range(n)]
        
        for r in range(m):
            for c in range(n): 
                pre_sum_row[r][c+1] = pre_sum_row[r][c] + grid[r][c] #prefix sum of row
                pre_sum_col[c][r+1] = pre_sum_col[c][r] + grid[r][c] #prefix sum of col
                
        def getSumRow(row, l, r):  
            return pre_sum_row[row][r + 1] - pre_sum_row[row][l]

        def getSumCol(col, l, r): 
            return pre_sum_col[col][r + 1] - pre_sum_col[col][l]
        
        for i in range(mcl, 1, -1):#each magic cube, desc
            for r in range(m - i +1): #sliding each col
                for c in range(n-i +1 ): #sliding each row
                    
                    diag, anti_diag = 0, 0
                    
                    for l in range(i):
                        diag += grid[r+l][c+l]#start from first col, first row
                        anti_diag += grid[r+l][c+i-1-l]#start from first col, last row
                        
                    ans = diag == anti_diag
                    
                    nr = r
                    nc = c
                    
                    while ans and nr < r + i: #check row
                        ans = diag == getSumRow(nr, c, c+i-1)
                        nr +=1
                    while ans and nc < c + i:
                        ans = diag == getSumCol(nc, r, r+i-1)
                        nc +=1
                    
                    if ans: return i
                    
        return 1
                    
            