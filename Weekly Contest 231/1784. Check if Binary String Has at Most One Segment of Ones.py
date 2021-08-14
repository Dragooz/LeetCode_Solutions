class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        #only can have a continuous '1' exists
        s = [a for a in s.split('0') if len(a)>=1 and a!=[]]
        
        return len(s) == 1