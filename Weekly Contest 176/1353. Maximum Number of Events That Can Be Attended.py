#Reference: https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/discuss/510263/JavaC%2B%2BPython-Priority-Queue

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        
        events.sort()
        n = len(events)
        pq = []
        
        i = 0
        ans = 0
        
        for j in range(10**5 + 1):
            
            while pq and pq[0] < j: #kick out expired events
                heappop(pq)
                
            while i<n and events[i][0] ==j:
                heappush(pq, events[i][1])
                i+=1
            
            if pq:
                heappop(pq) #get the earliest ending event
                ans+=1
        
        return ans