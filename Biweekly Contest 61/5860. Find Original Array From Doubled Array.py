from collections import Counter

class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        
        n = len(changed)
        
        if n % 2 != 0: #not even
            return []
        
        counter = Counter(changed)
        
        ans = []
        
        for key in sorted(counter.keys()):
            while counter[key] > 0:
                counter[key] -=1
                counter[key*2] -= 1
                
                ans.append(key)
            
            if counter[key*2] < 0:
                return []
            
        return ans