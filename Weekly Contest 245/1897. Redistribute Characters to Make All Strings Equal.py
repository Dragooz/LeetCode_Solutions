import collections
class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        
        dict_ = collections.defaultdict(int)
        
        words_length = len(words)
        
        for word in words:
            for char in word:
                dict_[char] += 1
                
        for key, val in dict_.items():
            if (val%words_length) != 0: #if it can't be distributed evenly
                return False
            
        return True