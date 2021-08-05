#Reference: https://leetcode.com/problems/queries-on-number-of-points-inside-a-circle/discuss/1163070/Short-and-Easy-Solution-w-Explanation-or-Distance-bw-point-and-Circle-Center by archit91
import math
class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        #each query, each points
        #if distance between points <= radius, count +1
        ans = []
        for x, y, r in queries:
            temp =0
            for xp, yp in points:
                if math.sqrt((xp - x)**2 + (yp - y)**2) <=r:
                    temp+=1
            ans.append(temp)
            
        return ans