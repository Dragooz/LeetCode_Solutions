#Reference from: https://leetcode.com/problems/longest-nice-substring/discuss/1074546/Python3-brute-force-and-divide-and-conquer ye15
#brute force
class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        ans = ''
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                
                if all(s[k].swapcase() in s[i:j] for k in range(i, j)):
                    ans = max(ans, s[i:j], key=len)
                    
        return ans
        
#OR divide and conquer

class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        #divide and conquer
        
        if not s: return ''
        
        ss = set(s)
        
        for i, c in enumerate(s):
            if c.swapcase() not in ss:
                s0 = self.longestNiceSubstring(s[:i])
                s1 = self.longestNiceSubstring(s[i+1:])
                
                return max(s0, s1, key=len)
                
        return s
    
        
