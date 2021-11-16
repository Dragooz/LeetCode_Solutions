#Reference: https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/discuss/609771/JavaC%2B%2BPython-Deques-O(N)

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:

        maxd = collections.deque()
        mind = collections.deque()
        i = 0
        for a in nums:
            while len(maxd) and a > maxd[-1]: maxd.pop()
            while len(mind) and a < mind[-1]: mind.pop()
            maxd.append(a)
            mind.append(a)

            if maxd[0] - mind[0] > limit:
                if maxd[0] == nums[i]: maxd.popleft()
                if mind[0] == nums[i]: mind.popleft()
                i += 1
        return len(nums) - i