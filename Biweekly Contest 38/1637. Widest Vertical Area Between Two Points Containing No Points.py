#Reference: https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points/discuss/917685/C%2B%2B-Ignore-Y

class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        
        points = sorted([i[0] for i in points])
        ans = 0
        for i in range(len(points)-1):
            ans = max(ans, points[i+1] - points[i])
            
        return ans