#Reference: https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/discuss/754721/C%2B%2BPython-7-line-Intuitive-Constant-Space-DP

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        
        #odd, odd+odd+odd, odd+odd+odd+odd+odd... -> odd_num//2 + 1
        #odd+even, odd+even+even.... --> above * num of even
        #odd+odd+odd+even....
        
        ans, even, odd = 0, 0 ,0
        mod = 10**9 +7 
        
        for i in arr:
            even+=1
            if i%2: #odd
                odd, even = even, odd
                
            ans = (ans+odd) % mod
                
                

        
        return ans