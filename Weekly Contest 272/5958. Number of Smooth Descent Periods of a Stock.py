class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        
        prefix = [i-j for i,j in zip(prices[:-1], prices[1:])]

        # print(prefix)
        
        n = len(prices)
        ans = n
        
        add = 0
        for i in range(len(prefix)):
            
            if prefix[i]==1:
                add+=1
                ans+=add
            else:
                add = 0
                    
        return ans
                    