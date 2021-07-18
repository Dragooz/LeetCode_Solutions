class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        
        ans = 0
        check_list = [j for j in brokenLetters]
        
        for t in text.split(' '):
            broke=False
            for char in check_list:
                if char in t: #broke
                    broke=True
                    break
            
            if broke==False:
                ans+=1
                
        return ans