#Reference: https://leetcode.com/problems/make-the-string-great/discuss/780991/Clean-Python-3-stack-O(N)

class Solution:
    def makeGood(self, s: str) -> str:
        
        result = []
        
        for char in s:
            if not result:
                result.append(char)
            elif (char.islower() and result[-1] == char.upper()) or (char.isupper() and result[-1] == char.lower()):
                result.pop(-1)
            else:
                result.append(char)
                
        return ''.join(result)