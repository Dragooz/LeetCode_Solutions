class Solution:
    def arrangeWords(self, text: str) -> str:
        
        splitted = text.split(' ')
        
        arr = sorted([(len(word), index) for index, word in enumerate(splitted)])
        
        ans = []
        
        for index, (i, j) in enumerate(arr):
            if index == 0:
                ans.append(splitted[j].capitalize())
            else:
                ans.append(splitted[j].lower())
            
        return ' '.join(ans)