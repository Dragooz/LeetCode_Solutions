#Reference: https://leetcode.com/problems/maximum-repeating-substring/discuss/952025/C%2B%2B-short-easy-using-find

class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        
        ans = 0
        temp = word
        while temp in sequence:
            ans += 1
            temp += word 
            
        return ans
            
            