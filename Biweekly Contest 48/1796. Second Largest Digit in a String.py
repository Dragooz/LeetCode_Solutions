class Solution:
    def secondHighest(self, s: str) -> int:
        
        s = [i for i in s if i.isnumeric()]
        s = list(set(s))
        s.sort()
        if len(s) >=2:
            return s[-2]
        else:
            return -1
        
        