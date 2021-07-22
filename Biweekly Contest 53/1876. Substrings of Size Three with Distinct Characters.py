class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        
        ans = 0
        for i in range(len(s) - 3 +1):
            chars = s[i: i+3]
            if chars[0] != chars [1]  and chars[0] != chars[2] and chars[1] != chars[2]:
                ans+=1
                
        return ans