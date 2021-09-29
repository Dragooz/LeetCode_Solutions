#https://leetcode.com/problems/number-of-sets-of-k-non-overlapping-line-segments/discuss/898830/Python-O(N)-Solution-with-Prove

class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        #Basically we just choose 2k points from n+k-1 and then group them in pairs to make segments.
        
        return comb(n+k-1, k*2) % (10**9+7)