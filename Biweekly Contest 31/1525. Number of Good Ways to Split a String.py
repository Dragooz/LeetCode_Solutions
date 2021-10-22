#Reference: https://leetcode.com/problems/number-of-good-ways-to-split-a-string/discuss/754719/Some-hints-to-help-you-solve-this-problem-on-your-own

class Solution:
    def numSplits(self, s: str) -> int:
        
        n = len(s)
        
        unique_p = set()
        unique_s = set()
        prefix = [0]*n
        suffix = [0]*n
        
        for i in range(n):
            unique_p.add(s[i])
            unique_s.add(s[n-i-1])
            
            prefix[i] = len(unique_p)
            suffix[n-i-1] = len(unique_s)
            
        ans =0 
        for i in range(1, n):
            if prefix[i-1] == suffix[i]:
                ans +=1
                
        return ans