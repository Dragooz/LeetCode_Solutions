#Reference: https://leetcode.com/problems/count-sorted-vowel-strings/discuss/1021493/One-line-solution-or-Math-or-No-DP-no-Big-Integers-or-O(1)-time-space

class Solution:
    def countVowelStrings(self, n: int) -> int:
        
        return math.comb(n+5-1, 5-1) #unordered with replacement, 5-1 because the last vowel fixed