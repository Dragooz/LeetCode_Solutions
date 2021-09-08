#Reference: https://leetcode.com/problems/maximum-binary-string-after-change/discuss/987510/python3-with-explanation

class Solution:
    '''
    final answer will always has <=1 zeros
    '''
    def maximumBinaryString(self, binary: str) -> str:
        zeros=binary.count('0')
        #if there exists less than 2 '0' in the string, meaning the string has already reached maximum, just return string itself.
        if zeros>1:
            #i stands for the number of '1' before the first '0'.
            i=binary.index('0')
            # The final string consists of i + (zeros-1) leading '1's, followed by a single '0' and the rest '1'.
            return '1'*(i+zeros-1)+'0'+'1'*(len(binary)-i-zeros)
        else:
            return binary

        