class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        
        n = len(s)
        ans = -1
        for i in range(n):
            for j in range(n-1, i, -1):
                if s[i] == s[j]:
                    ans = max(ans, len(s[i+1:j]))
                    break
                    
        return ans