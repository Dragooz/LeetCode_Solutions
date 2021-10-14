class Solution:
    def thousandSeparator(self, n: int) -> str:
        n = str(n)[::-1]
        new = ''
        
        ii =0
        for i in range(0, len(n)-3, 3):
            new += n[i:i+3] + '.'
            ii = i+3
            
        new += n[ii:]
        
        return new[::-1]