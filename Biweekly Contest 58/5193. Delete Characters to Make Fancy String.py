import re

class Solution:
    def makeFancyString(self, s: str) -> str:
        
        ans = ''
        
        for char in s:
            if len(ans) <2:
                ans+=char
                
            elif len(ans) >=2 and (ans[-1] != ans[-2] or ans[-1]!= char):
                ans += char
            
        return ans