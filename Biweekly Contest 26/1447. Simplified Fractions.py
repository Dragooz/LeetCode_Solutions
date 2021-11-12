class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        
        ans = []
        
        for i in range(2, n+1): #deno 
            for j in range(1, i+1): #nume
                
                if math.gcd(i,j) == 1: #simplified
                    ans.append(f'{j}/{i}')
                    
        return ans
                
        