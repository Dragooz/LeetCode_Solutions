class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        
        if k > len(s):
            return False
        
        if k == len(s):
            return True
        
        d = Counter(s)
        
        even, odd = 0, 0
        
        for key, val in d.most_common():
            if val % 2 == 0:
                even+=1
            else:
                odd+=1
                
        return odd <= k #can tolerate how many odds
        
        
        