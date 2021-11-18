#Reference: https://leetcode.com/problems/maximum-score-after-splitting-a-string/discuss/619000/Python-Simple.-Faster-than-94

class Solution:
    def maxScore(self, s: str) -> int:
        
        zeros = 1 if s[0] == '0' else 0 
        ones = s[1:].count('1')
        
        ans = zeros+ones
        
        for i in range(1, len(s)-1):
            
            if s[i] == '0':
                zeros+=1
            else:
                ones-=1
            
            ans = max(ans, zeros+ones)
            
        return ans