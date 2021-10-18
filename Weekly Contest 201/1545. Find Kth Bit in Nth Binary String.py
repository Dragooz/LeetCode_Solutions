#Reference: https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/discuss/781181/JavaC%2B%2BPython-Iterative-Solutions

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        
        def rev_invert(bit):
            return ''.join(['1' if i=='0' else '0' for i in bit][::-1])
        
        init = '0'
        for _ in range(n):
            init = init + '1' + rev_invert(init)

        return init[k-1]