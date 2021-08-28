#Reference from https://leetcode.com/problems/change-minimum-characters-to-satisfy-one-of-three-conditions/discuss/1032070/JavaC%2B%2BPython-Clean-Solution by lee215

from collections import Counter
class Solution:
    def minCharacters(self, a: str, b: str) -> int:
        
        m = len(a)
        n = len(b)
        
        c1 = Counter(ord(c) - ord('a') for c in a)
        c2 = Counter(ord(c) - ord('a') for c in b)
        
        #condition3
        res = (m+n) - max((c1+c2).values())
        
        for i in range(25):
            #prefix sum
            c1[i+1] += c1[i]
            c2[i+1] += c2[i]
            
            #condition1 - a<b 
            #(m-c1[i]) means number of operations needed to convert a to alpabets equal to 'i'th sequence
            #+c2[i] means how many operations needed to convert b to alphabets larger than 'i'th sequence
            res = min(res, (m-c1[i]) + c2[i] ) 
            
            #condition2 - a>b
            res = min(res, (n-c2[i]) + c1[i])
            
        return res
        
        