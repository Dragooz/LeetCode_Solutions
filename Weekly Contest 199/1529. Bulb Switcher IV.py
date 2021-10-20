class Solution:
    def minFlips(self, target: str) -> int:
        
        ans = 0
        bulb = []
        for c in target:
            if bulb and bulb[-1] == c:
                continue
                
            bulb.append(c)
            
        if bulb[0] == '0':
            return len(bulb) - 1
        else:
            return len(bulb)
            
            
            
            