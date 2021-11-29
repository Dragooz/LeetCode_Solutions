#Reference: https://leetcode.com/problems/minimum-cost-homecoming-of-a-robot-in-a-grid/discuss/1598941/JavaC%2B%2BPython-All-shortest-paths-have-the-same-cost

class Solution:
    def minCost(self, startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]) -> int:
        
        ans, [i,j], [x,y] = 0, startPos, homePos
        
        while i != x:
            if i > x:
                i-=1
            else:
                i+=1
            ans += rowCosts[i]
            
        while j != y:
            if j > y:
                j-=1
            else:
                j+=1
            ans += colCosts[j]
        
        return ans