class Solution:
    def concatenatedBinary(self, n: int) -> int:
        
        str_ = ''
        
        for i in range(1, n+1):
            str_ += str(bin(i))[2:]
            
        return int(str_, 2) % (10**9 + 7)