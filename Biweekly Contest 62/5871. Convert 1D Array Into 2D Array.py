class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        ans = []
        if m*n == len(original):
            for j in range(m):
                ans.append([original[i] for i in range(n)])
                original = original[n:]
                
        return ans