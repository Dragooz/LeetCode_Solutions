class Solution:
    def reorderSpaces(self, text: str) -> str:
        spaces = 0
        for tex in text:
            for te in tex:
                if te ==' ':
                    spaces+=1
        
        splitted = [i for i in text.split(' ') if i != '']
        nw = len(splitted)
        
        if nw != 1:
            spaces_ = spaces // (nw-1)
            remain = spaces % (nw-1)
        else:
            spaces_ = 0
            remain = spaces
        
        ans = (' '*spaces_).join(splitted)
        ans += (remain * ' ')

        return ans
        
        
        
        