#Reference: https://leetcode.com/problems/minimum-numbers-of-function-calls-to-make-target-array/discuss/805740/JavaC%2B%2BPython-Bit-Counts

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        # each '1' in binary of num means 1 operation 0
        # number of operation 1 = max(bit) -1
        
        max_len = 0
        num_1 = 0
        
        for num in nums:
            a = bin(num)
            
            num_1 += a.count('1')
            max_len = max(max_len, len(a))
            
        return num_1 + max_len - 1 -2 #-2 because binary has '0b' prefix
        