#Reference: https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/discuss/936436/JavaPython-3-Two-codes%3A-1-pass-and-2-passes-w-brief-explanation-and-analysis.

class Solution:
    def minimumDeletions(self, s: str) -> int:
        
        ans = suffix = 0
        for c in reversed(s):
            if c == "a": 
                suffix += 1 #turning a to b
            else: 
                ans = min(1 + ans, suffix) #either turning b to a or turning a to b 
                
        return ans
            
            