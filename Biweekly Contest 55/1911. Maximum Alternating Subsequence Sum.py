#reference:
#https://leetcode.com/problems/maximum-alternating-subsequence-sum/discuss/1298499/JavaC%2B%2BPython-Best-Time-to-Buy-and-Sell-Stock by lee215

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        
        #main idea:
        #keep track of odd and even (odd and even here means the alternating sum ended with odd/even index)
        #so i can deduce that even always >= odd
        #update odd with max(odd, even-a) 
        #update even with max(even, odd+a)
        
        odd = even = 0
        
        for num in nums:
            odd = max(odd, even-num)
            even = max(even, odd+num)
            
        return even