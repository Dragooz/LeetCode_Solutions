class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ans = [0] * len(s)
        
        for char, num in zip(s, indices):
            ans[num] = char
            
        return ''.join(ans)