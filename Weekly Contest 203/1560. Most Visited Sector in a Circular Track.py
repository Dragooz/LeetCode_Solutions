#Reference: https://leetcode.com/problems/most-visited-sector-in-a-circular-track/discuss/806814/JavaC%2B%2BPython-From-Start-to-End

class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        
        if rounds[0] <= rounds[-1]:
            return range(rounds[0], rounds[-1] + 1)
        else:
            return list(range(1, rounds[-1]+1)) + list(range(rounds[0], n+1))
