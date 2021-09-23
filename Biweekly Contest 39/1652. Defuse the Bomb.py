class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        code = code *2
        
        ans = []
        
        for i in range(n):
            
            if k>0:
                ans.append(sum(code[i+1:k+i+1]))
            elif k<0: 
                index = (n*2) - 1 - i
                ans.append(sum(code[index-(abs(k)): index]))
            else:
                return [0]* n
            
        if k<0:
            return ans[::-1]
        else:
            return ans
                