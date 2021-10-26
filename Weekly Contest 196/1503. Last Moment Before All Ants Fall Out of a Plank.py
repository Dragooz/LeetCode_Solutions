#Reference: https://leetcode.com/problems/last-moment-before-all-ants-fall-out-of-a-plank/discuss/720189/JavaC%2B%2BPython-Ants-Keep-Walking-O(N)

class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        
        return max(max(left or [0]), n - min(right or [n]))