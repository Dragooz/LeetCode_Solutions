import math
class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        
        highest_pow = math.ceil(math.log(n) / math.log(3))

        for i in range(highest_pow, -1, -1):
            
            if n >0 and n-pow(3,i) >= 0:
                n -= pow(3,i)
                
        return n==0
        