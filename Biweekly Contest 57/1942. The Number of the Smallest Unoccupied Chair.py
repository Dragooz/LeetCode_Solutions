#First Attempt, failed testcase (as didn't consider the chair occupied ordering)

class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        
        tar_start, _ = times[targetFriend]
        print('target:', times[targetFriend])
        chair = 0
        for time in times:
            strt, end = time
            if end <tar_start or strt > tar_start:
                continue
            print(time)
            if strt <tar_start <end:
                chair +=1
                
        return chair
            
#Second Attempt:
#Reference: https://leetcode.com/problems/the-number-of-the-smallest-unoccupied-chair/discuss/1359713/Python-Simple-Heap-Solution-with-Explanation by ajith6198 and SunnyvaleCA
from heapq import *
class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        
        n = len(times)
        
        e_chairs = [i for i in range(n)]
        seatings = [0] * n
        
        activity = []
        
        for index, (strt, end) in enumerate(times):
            activity.append([strt, True, index]) #start time, arriving, person
            activity.append([end, False, index]) #end time, arriving, person
            
        heapify(activity)
        
        while activity:
            
            _, arriving, p_index = heappop(activity)
            
            if arriving:
                if p_index == targetFriend:
                    return e_chairs[0]
                else:
                    seatings[p_index] = heappop(e_chairs) #remove the chair, record which person have that chairs
            else:
                heappush(e_chairs, seatings[p_index]) #push back the chair
        
            
