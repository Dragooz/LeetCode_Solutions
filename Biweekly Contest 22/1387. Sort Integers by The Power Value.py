class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        
        def odd(num):
            return 3*num +1
        
        def even(num):
            return num//2
        
        ans = []
        
        for i in range(lo, hi+1):
            num = i
            power = 0
            
            while num != 1:
                if num%2==0:
                    num = even(num)
                else:
                    num = odd(num)
                    
                power+=1
                    
            heappush(ans, (power, i))
                    
        for i in range(k):
            final = heappop(ans)[1]
        
        return final