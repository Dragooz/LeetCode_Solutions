#Reference from : https://leetcode.com/problems/count-number-of-homogenous-substrings/discuss/1064530/JavaC%2B%2BPython-Straight-Forward lee215

class Solution:
    def countHomogenous(self, s: str) -> int:
        
        i = 0
        count = 1
        ans = 1
        mod = 10**9 +7
        
        while i <len(s) - 1:
            
            char = s[i]
            if char == s[i+1]:
                count +=1
            else:
                count = 1
            
            ans += count
            i+=1
            
        return ans % mod

            
            
        
            
            