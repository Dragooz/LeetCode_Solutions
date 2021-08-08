class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        for word in words:
            if s == '':
                return True
            if s[0:len(word)] == word:
                s = s[len(word):]
            else:
                return False
        
        if s == '':
            return True
        else:
            return False
        