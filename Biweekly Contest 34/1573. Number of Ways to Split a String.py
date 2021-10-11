#Reference: https://leetcode.com/problems/number-of-ways-to-split-a-string/discuss/830536/Python-or-One-pass-or-Explained-and-Visualised

class Solution:
    def numWays(self, s: str) -> int:
        n = len(s)
        index = []
        sum_ = 0
        
        for i, char in enumerate(s):
            if char == '1':
                sum_ += 1
                index.append(i)
        
        if sum_%3 != 0:
            return 0
        
        num_split = sum_//3

        if index:
            return (index[num_split]-index[num_split-1]) * (index[num_split*2]-index[num_split*2-1]) % (10**9 +7)
        else:
            return ((n-2) * (n-1) // 2  )% (10**9 +7)