import math
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        nums.sort()
        
        min_ = nums[0]
        max_ = nums[-1]
        
        return math.gcd(min_, max_)