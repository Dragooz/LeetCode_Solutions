class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        
        knowledge = dict(knowledge)
        ans = ''
        
        open_brac = False
        temp = ''
        
        for char in s:
            
            if char == '(':
                open_brac = True
                continue
            
            if char == ')':
                open_brac = False
                ans += knowledge.get(temp, '?') #get temp key if exist, else return '?'
                temp = ''
                continue
                
            if open_brac:
                temp += char
            else:
                ans += char
                
        return ans