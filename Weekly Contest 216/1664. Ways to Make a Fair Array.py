#Reference: https://leetcode.com/problems/ways-to-make-a-fair-array/discuss/944377/Clean-Python-3-prefix-sum-O(N)

class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        
        even_remain, odd_remain = sum(nums[::2]), sum(nums[1::2]) #sum of even, sum of odd
        
        even_curr, odd_curr, result = 0, 0, 0 #track back the removed numbers
        
        for i, num in enumerate(nums):
            if i % 2 == 0: #if even
                even_remain -= num #remove the num from even_remain
                result += (even_curr + odd_remain == odd_curr + even_remain) #see whether left = right
                even_curr += num #track back the removed num
            else: #if odd
                odd_remain -= num #remove the num from odd remain
                result += (even_curr + odd_remain == odd_curr + even_remain) #see whether left = right
                odd_curr += num #track back the removed num
        return result
        