import re
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s = s.lower()
        
        n = len(s) // 2
        
        return len(re.sub(r'[^aeiou]', '', s[:n])) == len(re.sub(r'[^aeiou]', '', s[n:]))
        