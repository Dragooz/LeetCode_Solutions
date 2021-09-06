#First Attempt: TLE

from collections import Counter
import math

class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        
        counter = Counter(deliciousness)
        
        combination = list(counter.keys())
        n = len(combination)
        ans = 0
        
        for i in range(n):
            f = combination[i]
            for j in range(i, n):
                s = combination[j]
                if f+s > 0 and math.log2(f+s) % 1 == 0: #exist
                    if f != s:
                        ans += (counter[f] * counter[s])
                    else:
                        ans += sum([i for i in range(1, counter[f])])
                        
        return ans % (10**9 +7)

#Second Attempt: Reference: https://leetcode.com/problems/count-good-meals/discuss/999170/Python3-frequency-table

from collections import Counter
import math

class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
    
        ans = 0
        freq = defaultdict(int)
        for x in deliciousness: 
            for k in range(22): 
                ans += freq[2**k - x] #in range 22 means number from 0 to 21 (as constraints is <= 2**20)
            freq[x] += 1
        return ans % (10**9 +7)