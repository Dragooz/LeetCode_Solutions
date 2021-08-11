import collections
from math import comb

class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        #j must bigger than i
        #if reverse diff of the two nums similar, proceed 
        
        def rev(val):
            return int(str(val)[::-1])
# ----------------------------first attempt------------------------------------
        diff = dict(collections.Counter([val-rev(val) for val in nums])) #don't put abs here then its okay.
        diff = [val for k, val in diff.items() if val >=2]
        ans = 0
        for d in diff:
            ans = (ans + comb(d, 2))% (10**9 + 7)
        return ans
# ----------------------------first attempt------------------------------------

# ---------------------------second attempt------------------------------------
# Reference from https://leetcode.com/problems/count-nice-pairs-in-an-array/discuss/1140639/JavaC%2B%2BPython-Straight-Forward by lee215
#         counter = collections.Counter()
#         ans = 0
#         for val in nums:
#             # diff = abs(val-rev(val))
#             diff = (val-rev(val)) #no need abs here because -21 and 21 is diff set.
#             ans += counter[diff] #first occurance doesn't count, so it begin with 0
#             counter[diff] += 1 #here, update the val into 1 so that the next occur ans+=1
            
#         return ans % (10**9 + 7)
