#First try using dp, depth first search, failed

class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        #main idea:
        #i + minJump <= j <= min(i + maxJump, s.length - 1)
        #s[j] == '0'
        
        jump_range = [k for k in range(minJump, maxJump+1)]
        
        def dp(s_new):
            if len(s_new) == 1:
                return True
            for j in jump_range: #i+jr = j
                # print('j:', j)
                # print('s_new:', s_new)
                # print('minJump <= j:', minJump <= j)
                # print('j <= min(maxJump, len(s_new)-1)', j <= min(maxJump, len(s_new)-1))
                if minJump <= j <= min(maxJump, len(s_new)-1) and s_new[j] == '0':
                    temp = dp(s_new[j:]) #call only but not returning
                    if temp == True: #if get len(s) == 1
                        return True

        ans = False
        ans = dp(s)
        
        return ans

#Reference: https://leetcode.com/problems/jump-game-vii/discuss/1224804/JavaC%2B%2BPython-One-Pass-DP by lee215

class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        #main idea:
        #sliding window (either one in the window can reach is fine.)
        
        dp = [c == '0' for c in s] #position is reachable or not
        pre = 0 #number of places it can jump in the sliding window
        
        for i in range(1, len(s)):
            if i >= minJump: #in window, +1 if it can jump
                pre += dp[i - minJump]
            if i > maxJump: #out of window
                pre -= dp[i - maxJump - 1]
                
            dp[i] = dp[i] & (pre > 0) #if it can be reach, and the character is able to jump to
            
        return dp[-1]