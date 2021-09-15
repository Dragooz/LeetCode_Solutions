#Reference: https://leetcode.com/problems/minimum-moves-to-make-array-complementary/discuss/952773/PythonJava-simple-O(max(n-k))-method

from collections import Counter

class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        
        n = len(nums)
        delta = Counter()
        
        for i in range(n // 2):
            a, b = nums[i], nums[n -1 - i]
            delta[2] += 2
            delta[min(a, b) + 1] -= 1
            delta[a + b] -= 1
            delta[a + b + 1] += 1
            delta[max(a, b) + limit + 1] += 1
        
        curr = 0            
        res = math.inf
        for i in range(2, 2 * limit + 1):
            curr += delta[i]
            res = min(res, curr)
        return res   
    