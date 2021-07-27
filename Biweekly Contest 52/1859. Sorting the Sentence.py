class Solution:
    def sortSentence(self, s: str) -> str:
        s = s.split(' ')
        sl = len(s)
        ans = [''] * sl
        
        for char in s:
            ans[int(char[-1]) -1] = char[:-1]
            
        return ' '.join([i for i in ans])