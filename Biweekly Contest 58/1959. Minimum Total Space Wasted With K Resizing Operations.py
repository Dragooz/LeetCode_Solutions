#Copied from: https://leetcode.com/problems/minimum-total-space-wasted-with-k-resizing-operations/discuss/1389247/C%2B%2BJavaPython-Simple-Top-down-DP-Clean-and-Concise by hiepit
#quite confusing to understand, check back in the future.
from functools import lru_cache

class Solution:
    def minSpaceWastedKResizing(self, nums: List[int], k: int) -> int:
        n, INF = len(nums), 200 * 1e6

        @lru_cache(None)
        def dp(i, k):
            if i == n: return 0 #base case reached
            if k == -1: return INF #invalid
            ans = INF
            maxNum = nums[i]
            totalSum = 0
            for j in range(i, n): #for every index in nums
                maxNum = max(maxNum, nums[j]) #get the max num in every loop (so that it doesn't need to be sorted)
                totalSum += nums[j] #the total along the way
                wasted = maxNum * (j - i + 1) - totalSum #get the wasted space
                ans = min(ans, dp(j + 1, k - 1) + wasted)#either the previous answer, or answer after using the k.
            return ans

        return dp(0, k)