#Reference: https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/discuss/531850/Python-solution-in-O(n)-time-and-O(1)-space-explained

class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowels = {'a': 1, 'e': 2, 'i': 4, 'o': 8, 'u': 16}
        
        d, n, r = {0: -1}, 0, 0 #seen, mask, res
        
        for i, c in enumerate(s):
            if c in vowels:
                n ^= vowels[c]
            if n not in d:
                d[n] = i
            else:
                r = max(r, i - d[n]) #to know the range
                
        return r