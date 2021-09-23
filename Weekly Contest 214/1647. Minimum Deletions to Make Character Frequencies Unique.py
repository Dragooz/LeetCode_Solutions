#Reference: https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/discuss/927549/C%2B%2BJavaPython-3-Greedy

from collections import Counter

class Solution:
    def minDeletions(self, s: str) -> int:
        
        count = Counter(s)
        
        values = list(count.values())
        
        seen = set()
        
        ans = 0
        
        for i in values:
            temp = i
            while temp>0 and temp in seen:
                temp -= 1
                ans+=1
                
            seen.add(temp)
            
        return ans
            
            