#first attempt:

class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        dp = [0]*(len(obstacles))
        dp[0] = 1
        for i in range(1, len(obstacles)):
            temp = obstacles[:i+1]
            
            j = i-1
            while j>=0 and temp[j] > temp[-1]: #if latter smaller than former, invalid
                j -= 1
            
            if j < 0:
                dp[i] = 1
            else:
                dp[i] = max(dp[:j+1]) + 1
        
        return dp

#Second attempt:
#Reference: https://leetcode.com/problems/find-the-longest-valid-obstacle-course-at-each-position/discuss/1390162/JavaC%2B%2BPython-Mono-Increasing-Stack by lee215

class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:

        mono, res = [], []
        for ob in obstacles:
            i = bisect.bisect(mono, ob) #return the right most position of ob that should be inserted so that the mono is in ascending.
            res.append(i + 1) #if inserted in index 1, means it has 0 and 1, which is two subs.
            if i == len(mono): #if its inserted at the right most of the mono, means it increase the number of mono.
                mono.append(0)
            print(mono[i], 'mono')
            print(ob, 'ob')
            mono[i] = ob #if no obstacle appended into mono, then the ob should replace the previous mono[i] to result in smaller.
        return res