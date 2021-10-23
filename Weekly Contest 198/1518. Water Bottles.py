class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        
        # numBottles + nB//nE + (nB%nE)
        
        ans = 0
        emptyBottles = 0
        
        while numBottles > 0:
            ans += numBottles
            totalBottles = numBottles + emptyBottles
            if totalBottles >= numExchange:
                numBottles = totalBottles//numExchange
                emptyBottles = totalBottles%numExchange
            else:
                break
        return ans