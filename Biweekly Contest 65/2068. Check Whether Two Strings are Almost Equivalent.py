class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        
        unique_word = set(word1)
        for i in set(word2):
            unique_word.add(i)
        
        w1c = Counter(word1)
        w2c = Counter(word2)
        
        res = 0
        
        for u in unique_word:
            res = max(res, abs(w1c[u] - w2c[u]))
            
        return res <=3
        
        
        
        