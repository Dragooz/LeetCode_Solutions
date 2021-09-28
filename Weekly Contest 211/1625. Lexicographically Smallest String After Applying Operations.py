#Reference: https://leetcode.com/problems/lexicographically-smallest-string-after-applying-operations/discuss/899471/Python-Easy-to-understand

class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        #brute force
        def add(s):
            new_str = ''
            for i in range(len(s)):
                if i %2 == 0:
                    new_str += s[i]
                else:
                    new_str += str(int(s[i]) + a)[-1]
                    
            return new_str
        
        def rotate(s):
            return s[len(s)-b:] + s[0:len(s)-b]
        
        seen = set()
        need = list()
        
        need.append(s)
        
        while need:
            cur = need.pop()
            
            if cur not in seen:
                seen.add(cur)
                need.extend([add(cur), rotate(cur)]) #extend = multiple append in one line
                
        return min(seen)
                