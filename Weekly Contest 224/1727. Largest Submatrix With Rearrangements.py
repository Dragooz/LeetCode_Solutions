#Reference: https://leetcode.com/problems/largest-submatrix-with-rearrangements/discuss/1020708/Python-9-lines-or-Easy-to-understand-explanation-with-pictures-or-Faster-than-100 
#Failed Test case
class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        
        m = len(matrix)
        n = len(matrix[0])
        
        height = [0]* n
        
        ans = 0
        for row in range(m):
            for col in range(n):
                if matrix[row][col]:
                    height[col] += 1
                else:
                    height[col] = 0
                    
                    
        curr = sorted(height) #sort and reverse 
        print(curr)
        for i in range(n): #if curr = [3,2,0] <<means its either 3x1, 2x2, or 1x3(not possible)
            ans = max(ans, curr[i] * (n-i))
        
        return ans
    
#Second
#Reference: https://leetcode.com/problems/largest-submatrix-with-rearrangements/discuss/1154764/Python-solution-easy-understanding-with-comments

class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        
        m = len(matrix)
        n = len(matrix[0])
        
        ans = 0
        row=0
        for row in range(1,m):
            for col in range(n):
                if matrix[row][col]:
                    matrix[row][col] += matrix[row-1][col]

        ans = 0
        for i in range(m): # for every row we sort the list in ascending order
            matrix[i].sort(reverse=True)
            for j in range(n): 
                ans = max(ans, (j+1)*matrix[i][j]) # record the largest submatrix
        return ans
    
    

