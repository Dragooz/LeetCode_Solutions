#Reference: https://leetcode.com/problems/maximum-profit-of-operating-a-centennial-wheel/discuss/866409/Java-Simple-O(N)-greedy

class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        
        sc = 0
        prof = 0
        turned = 0
        
        ans = 0
        max_run = -1
        
        while sc>0 or customers:
            
            if customers:
                sc+= customers.pop(0)

            min_ = min(4, sc)
            prof += (min_*boardingCost) - runningCost
            sc -= min_
            
            turned +=1
            
            if prof > ans:
                max_run = turned
                ans = prof

        return max_run