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