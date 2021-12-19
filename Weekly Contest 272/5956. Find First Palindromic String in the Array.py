class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        
        for word in words:
            flag=True
            
            for i in range(len(word) //2):
                if word[i] != word[-i-1]:
                    flag=False
                    break
                    
            if flag:
                return word
            
        return ""
                