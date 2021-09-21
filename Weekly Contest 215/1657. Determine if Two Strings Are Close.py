from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        
        a = Counter(word1)
        b = Counter(word2)
        
        if sorted(set(a.keys())) == sorted(set(b.keys())):
            for y, z in zip(sorted(list(a.values())), sorted(list(b.values()))):
                if y != z:
                    return False
        else:
            return False
            
        return True
        