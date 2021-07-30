class Solution:
    def replaceDigits(self, s: str) -> str:
        
        ans = ''
        if len(s) % 2== 0:
            for i in range(0, len(s), 2):
                ans += s[i] + chr(ord(s[i]) + int(s[i+1]))
        else: #odd
            for i in range(0, len(s)-1, 2):
                ans += s[i] + chr(ord(s[i]) + int(s[i+1]))
            ans += s[-1]
        return ans