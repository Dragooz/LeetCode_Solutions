class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        
        ans = []
        ans.append(first)
        
        for i, e in enumerate(encoded):
            ans.append(e^ans[i])
            
        return ans