#Reference: https://leetcode.com/problems/minimum-non-zero-product-of-the-array-elements/discuss/1403913/Python-math-oneliner-with-proof-explained by DBabichev

class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        
        mod = 10**9 +7
        # p=3, there's three '6's and one '7'. p=4, there's seven '14's and one '15' and so on so forth.
        ans = (pow(2**p -2, 2**(p-1)-1, mod) * (2**p -1)) % mod 
      
        return ans