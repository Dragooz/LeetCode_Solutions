#Reference: https://leetcode.com/problems/minimum-number-of-frogs-croaking/discuss/586653/C%2B%2B-Python-Java-Lucid-code-with-documened-comments-%2B-Visualization

class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        
        c, r, o, a, k = 0, 0, 0, 0, 0
        in_use = 0
        ans = 0
        
        for d in croakOfFrogs:
            
            if d == 'c':
                c +=1
                in_use +=1
            elif d == 'r':
                r +=1
            elif d == 'o':
                o+=1
            elif d == 'a':
                a+=1
            elif d =='k':
                k+=1
                in_use-=1
            
            ans = max(ans, in_use)
            
            if c<r or r<o or o<a or a<k:
                return -1
            
        if c == r == o == a == k:
            return ans
        else:
            return -1
        