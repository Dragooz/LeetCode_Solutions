#Reference: https://leetcode.com/problems/minimum-deletion-cost-to-avoid-repeating-letters/discuss/831588/JavaC%2B%2BPython-Straight-Forward

class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:

        ans, max_cost = 0, 0
        
        for i in range(len(s)):
            if i>0 and s[i] != s[i-1]:
                max_cost = 0
                
            ans += min(max_cost, cost[i]) #we always pick smaller cost
            max_cost = max(max_cost, cost[i]) #update max_Cost
                
        return ans
