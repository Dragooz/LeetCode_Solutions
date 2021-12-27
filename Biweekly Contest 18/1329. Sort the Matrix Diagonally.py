#Reference: https://leetcode.com/problems/sort-the-matrix-diagonally/discuss/489749/JavaPython-Straight-Forward

class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        
        n, m = len(mat), len(mat[0])
        dlist = defaultdict(list)
        
        for i in range(n):
            for j in range(m):
                dlist[i-j].append(mat[i][j])
                
        for k in dlist:
            dlist[k].sort(reverse=True)
            
        for i in range(n):
            for j in range(m):
                mat[i][j] = dlist[i-j].pop()
                
        return mat