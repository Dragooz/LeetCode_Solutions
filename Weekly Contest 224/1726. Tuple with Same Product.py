#Reference: https://leetcode.com/problems/tuple-with-same-product/discuss/1020585/C%2B%2B-Hash-Table-or-Time-O(N2)-Space-O(N2)-or-100%2B100 by GoogleNick

from collections import defaultdict
 
'''
No of ways of arranging (a* b) = 2 {(a,b),(b,a)}
No of ways of arranging (c*d) = 2 {(c,d),(d,c)}
No of wasy of arranging (a*b) and (c*d) = 2  {(a*b)=(c*d), (c*d)=(a*b)}
Hence the total no of ways = 2*2*2 =8 

'''
    
    
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        freq_table = defaultdict(int)
        
        ans = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                
                ans +=  freq_table[nums[i] * nums[j]]
                freq_table[nums[i] * nums[j]] += 1
                
        return ans*8