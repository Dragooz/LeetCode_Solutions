#first attempt failed
from functools import cache
class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        #start from middle lane
        #whenever meet obstacles in the lane, call a two dp of two different length, choose the min and +1
        #reach destination, stop.
        lanes = [1,2,3]
        
        @cache
        def dp(cur_lane, cur_index):
            
            if obstacles[cur_index] == cur_lane: #step on obstacle. #impossible
                return 5* (10**5) +1
            
            while cur_index+1 < len(obstacles) and obstacles[cur_index+1] != cur_lane: #no obstacles, then move forward
                cur_index +=1
                
            if cur_index == len(obstacles) -1: #reach 
                return 0
            #here, the next step is obstacle, so go to another two lanes
            lane_one, lane_two = [i for i in lanes if i!=cur_lane]
            
            return min(dp(lane_one, cur_index), dp(lane_two, cur_index))+1
            
        return dp(2, 0)

#second attempt:
#Reference: https://leetcode.com/problems/minimum-sideway-jumps/discuss/1152665/JavaC%2B%2BPython-DP-O(1)-space by lee215
class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        #dp
        
        dp = [1,0,1] # side jump needed to perform to complete at lane 1, 2, and 3 (the frog start at lane 2)
        
        for ob in obstacles:
            if ob: #means it has obstacles
                dp[ob-1] = 5*10**5 +1 #the lane become impossible
                
            for i in range(3): #3lanes
                if i+1 != ob: #that lane no obstacles
                    dp[i] = min(dp[i], dp[(i+1)%3]+1, dp[(i+2)%3]+1 )# get back itself, or another two lanes min +1.
        
        return min(dp)

