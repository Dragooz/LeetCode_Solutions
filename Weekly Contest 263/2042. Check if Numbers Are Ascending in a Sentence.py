#Reference: https://leetcode.com/problems/check-if-numbers-are-ascending-in-a-sentence/discuss/1525219/Python3-2-line

class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        def isinteger(a):
            try:
                int(a)
                return True
            except ValueError:
                return False

        nums = [int(i) for i in s.split(' ')  if isinteger(i)]
        
        return all(nums[i-1] < nums[i] for i in range(1, len(nums)))