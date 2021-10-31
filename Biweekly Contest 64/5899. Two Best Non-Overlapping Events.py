#Reference: https://leetcode.com/problems/two-best-non-overlapping-events/discuss/1549128/Python%3A-Actually-simple-with-heap

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        
        events.sort()
        n = len(events)
        
        ans = 0
        max_val = 0
        interval_seen = []
        
        for st, et, val in events:
            heappush(interval_seen, (et, val))

            while interval_seen and interval_seen[0][0] < st: #end, then another event start
                ett, vall = heappop(interval_seen)
                max_val = max(max_val, vall)
                
            ans = max(ans, max_val + val)
                    
        return ans