#Reference from https://leetcode.com/problems/find-kth-largest-xor-coordinate-value/discuss/1032010/Detailed-Explanation-or-C%2B%2B-Solution-or-Easy-Implementation by Invulnerable

class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        
        n = len(matrix) #row
        m = len(matrix[0]) #col
        
        prefix = [0] * (n*m)
        
        #horizontally transform
        for i in range(n):
            for j in range(1, m):
                matrix[i][j] = matrix[i][j-1] ^ matrix[i][j]
        
        #vertically transform
        for j in range(m):
            for i in range(1, n):
                matrix[i][j] = matrix[i-1][j] ^ matrix[i][j]
                
        ans = sorted([i for j in matrix for i in j])[::-1]
        
        return ans[k-1]
        
        