#Reference: https://leetcode.com/problems/matrix-diagonal-sum/discuss/837795/Python-O(n)-by-iteration-w-Comment

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        
        n = len(mat)
        
        ans = 0
        if n%2 == 0:
            for i in range(n):
                ans+= mat[i][i]
                ans+= mat[n-1-i][i]
        else:
            for i in range(n):
                ans+= mat[i][i]
                ans+= mat[n-1-i][i]     
                
            mid = (n) // 2
            ans -= mat[mid][mid]
            
        return ans