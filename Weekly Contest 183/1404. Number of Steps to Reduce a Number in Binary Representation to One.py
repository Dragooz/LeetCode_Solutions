#Reference: https://leetcode.com/problems/longest-happy-string/discuss/564277/C%2B%2BJava-a-greater-b-greater-c

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int, aa = 'a', bb = 'b', cc = 'c') -> str:
        
        if a < b:  # Make sure a >= b by swapping a and b
            return self.longestDiverseString(b, a, c, bb, aa, cc)
        elif b < c: # Make sure b >= c by swapping b and c
            return self.longestDiverseString(a, c, b, aa, cc, bb)
        elif b == 0:  # Now a >= b >= c. If b == 0, we have c == 0, and a >= 0.
            return min(a, 2) * aa   # We construct the happy string with the remaining `a`
        
        """ 
        Now the basic idea is to concatenate 2 `a` with 1 `b`, so that the most frequent interger `a` can be consumed as much as possible. 
        But we have to consider the edge cases, such as `a == 1` or `a == b` or `b == 0`

        If a == 1, we can only repeat it for 1 time. Otherwise, we repeat it for 2 times. In short, we have `min(a, 2)`.
        """
        repeat_a = min(a, 2)  
        
        """
        if a == b --> we concatenate 2 `a` with 1 `b` (e.g., "aab")
        `b` > `a` now --> we swap `a` and `b` in the next call 
        --> we concatenate 2 `a` with 1 `b` (e.g., "bba") --> we have "aabbba", which is not a happy string
        So we set repeat_b = 0 if a == b.
        Now we consider the case where a != b, including two sub-cases: a >= 2, and a == 1.
        -subcase 1 (a >= 2): If b >= 1, we can repeat `b` for 1 time. If b == 0, we cannot repeat `b`. In short, we have `min(b, repeat_a-1)`
        -subcase 2 (a == 1): b == 1 or b == 0 now. We can just repeat `b` for b time, but the expression `min(b, repeat_a-1)` is also acceptable.
        """
        repeat_b = 0 if a == b else 1 #b is not gonna be 0
        
        return aa * repeat_a + bb * repeat_b + self.longestDiverseString(a-repeat_a, b-repeat_b, c, aa, bb, cc)