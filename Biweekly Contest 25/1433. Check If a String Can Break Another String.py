class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        
        s1 = sorted([ord(s) -97 for s in s1], reverse=True)
        s2 = sorted([ord(s) -97 for s in s2], reverse=True)
        
        s1_bool = True
        s2_bool = True
        
        for one, two in zip(s1, s2):
            if one > two:
                s2_bool = False
            elif two > one:
                s1_bool = False
            
        return s1_bool or s2_bool