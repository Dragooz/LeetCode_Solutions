#Reference: https://leetcode.com/problems/decode-xored-permutation/discuss/1031107/JavaC%2B%2BPython-Straight-Forward-Solution

class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        # the main objective is to find a1 (so that we can proceed to get the decoded perm)
        # a1^a2^a3 ^ (a1^a2) = a3
        # encoded = [a1^a2, a2^a3, a3^a4...]
        # so i can get a1^a2, a1^a3, a1^a4 by a1^a2 ^ a2^a3, a1^a3 ^ a3^a4 ....
        # we know that a1^a2 ^ a1^a3 ^ (a1^a2^a3) = a1 <<master formula to get a1
        # since its from 1 to n
        
        longest = 0
        
        for i in range(1, len(encoded)+1+1): #first +1 is to get perm, and second is to make it inclusive
            longest ^= i
            
        cur = 0
        for e in encoded:
            cur ^= e #first loop will be a1^a2, second will be a1^a2 ^ a2^a3 = a1^a3
            longest ^= cur #proceed to use master formula to get a1
            
        ans = [longest]
        
        for e in encoded:
            ans.append(e^ans[-1])
            
        return ans