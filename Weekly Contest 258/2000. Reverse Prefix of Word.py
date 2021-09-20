class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        
        try:
            index = word.index(ch)
        except:
            return word
        
        return word[0:index+1][::-1] + word[index+1:]