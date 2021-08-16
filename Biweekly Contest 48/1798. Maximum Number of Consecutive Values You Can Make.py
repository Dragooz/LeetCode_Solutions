#Reference: https://leetcode.com/problems/maximum-number-of-consecutive-values-you-can-make/discuss/1118770/JavaC%2B%2BPython-Accumulate-the-Coins by lee215

class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        coins.sort()
        
        ans =1
        
        for coin in coins:
            if ans < coin: return ans
            ans+= coin
            
        return ans