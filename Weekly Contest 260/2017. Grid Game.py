#Reference: https://leetcode.com/problems/grid-game/discuss/1486340/C%2B%2BJavaPython-Robot1-Minimize-TopSum-and-BottomSum-of-Robot-2-Picture-Explained

class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        
        n = len(grid[0])
        
        ans = math.inf
        
        bottom_sum = 0
        top_sum = sum(grid[0])
        
        for i in range(n):
            
            top_sum -= grid[0][i]
            
            ans = min(ans, max(top_sum, bottom_sum)) #first case bottom = 0
            
            bottom_sum += grid[1][i]
            
        return ans