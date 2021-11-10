class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        
        for index, s in enumerate(sentence.split(' ')):
            if searchWord == s[:len(searchWord)]:
                return index+1
            
        return -1