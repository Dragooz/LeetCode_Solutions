class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        
        A = []
        B = []
        
        a = 0
        b = 0
        for c in colors:
            if c == 'A':
                if b>2:
                    B.append(b-2)
                b = 0
                a+=1
            else:
                if a>2:
                    A.append(a-2)
                a = 0
                b+=1
        
        if a!= 0:
            A.append(max(0, a-2))
        if b!=0:
            B.append(max(0, b-2))
                
        return sum(A) > sum(B)
        