#Reference: https://leetcode.com/problems/count-submatrices-with-all-ones/discuss/721999/Python3-O(MN)-histogram-model
class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        
        m, n = len(mat), len(mat[0])
        
        for i in range(m): #make it to histogram
            for j in range(n):
                if mat[i][j] and i>0:
                    mat[i][j] += mat[i-1][j]
                
        ans = 0
        for i in range(m): #row by row
            
            stack = []
            cnt = 0
            
            for j in range(n):
                
                while stack and mat[i][stack[-1]] > mat[i][j]: #popping height of stack to make it the same with mat[i][j]
                    jj = stack.pop()
                    kk = stack[-1] if stack else -1
                    cnt -= (mat[i][jj] - mat[i][j])*(jj-kk)
                    
                cnt += mat[i][j]
                ans += cnt
                stack.append(j)
                
        return ans