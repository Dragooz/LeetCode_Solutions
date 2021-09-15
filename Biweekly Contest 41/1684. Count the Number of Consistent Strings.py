class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        
        ans= 0
        
        for word in words:
            ans += all(w in allowed for w in word)
            
        return ans
                