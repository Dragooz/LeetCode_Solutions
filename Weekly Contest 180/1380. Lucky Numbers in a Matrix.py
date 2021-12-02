class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        
        col = [min(matrix[i]) for i in range(len(matrix))]
        
        inverted_mat = [i for i in zip(*matrix)]
        
        row = [max(inverted_mat[i]) for i in range(len(inverted_mat))]
        
        return set(col).intersection(set(row))