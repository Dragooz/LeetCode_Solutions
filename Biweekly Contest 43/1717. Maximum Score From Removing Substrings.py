#Reference: https://leetcode.com/problems/maximum-score-from-removing-substrings/discuss/1008917/Python-O(n)-time-O(1)-space-straightforward-greedy-solution

from collections import Counter

class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        #x = ab, y = ba
        #x always > y, remove ab first
        
        a = 'a'
        b = 'b'
        
        if y > x:
            x , y = y, x
            b, a = a, b
        
        ans = 0
        seen = Counter()
        
        for char in s+'#':
            if char in 'ab':
                if char == b and seen[a] > 0:
                    ans += x
                    seen[a]-=1
                else:
                    seen[char]+=1
            else:
                ans += y*min(seen[a], seen[b])
                seen = Counter()
        
        return ans
        