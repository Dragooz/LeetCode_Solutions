class Solution:
    def minimumLength(self, s: str) -> int:
        s= list(s)
        
        while len(s) > 1:
            char = s[0]
            
            if s[-1] == char:
                while s and s[-1] == char:
                    s.pop(-1)
                    # print(s)

                while s and s[0] == char:
                    s.pop(0)
            else:
                return len(s)
            
        return len(s)

# OR
#Reference from https://leetcode.com/problems/minimum-length-of-string-after-deleting-similar-ends/discuss/1052535/Python-Easy-and-Concise by lee215 
class Solution:
    def minimumLength(self, s: str) -> int:
        
        while len(s) > 1 and s[0] == s[-1]:
            s = s.strip(s[0])
        return len(s)