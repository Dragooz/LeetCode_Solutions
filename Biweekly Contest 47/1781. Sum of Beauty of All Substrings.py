#Reference: https://leetcode.com/problems/sum-of-beauty-of-all-substrings/discuss/1096392/Python3-freq-table by ye15

class Solution:
    def beautySum(self, s: str) -> int:
        #get all substring
        #cal
        ans = 0
        for i in range(len(s)):
            freq = [0] * 26 #26 letters
            for j in range(i, len(s)):
                freq[ord(s[j]) - 97] += 1
                ans += max(freq) - min(x for x in freq if x) #we want non-zero min, if only 1 val exist, then it is the max freq itself
                
        return ans