#Reference: https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/discuss/516977/JavaC%2B%2BPython-Easy-and-Concise

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        
        ans = 0
        i = 0
        
        count = {j:0 for j in 'abc'}
        
        for j in range (len(s)):
            count[s[j]] += 1
            
            while all(count.values()):
                count[s[i]] -= 1
                i+=1
                
            ans += i
            
        return ans