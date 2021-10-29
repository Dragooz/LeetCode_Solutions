#Reference: https://leetcode.com/problems/avoid-flood-in-the-city/discuss/697687/A-Set-and-A-Map-Lucid-code-with-documented-comments.

class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        
        lake = dict()
        dry_days = []
        ans = []
        
        for day, rain in enumerate(rains):
            
            if rain == 0:
                dry_days.append(day)
                ans.append(1)
                continue
                
            if rain in lake:
                ans.append(-1)
                prev_day = lake[rain]
                
                chosen_day = bisect.bisect(dry_days, prev_day)
                
                if chosen_day > (len(dry_days) -1):
                    return []
                else:
                    lake[rain] = day
                    ans[dry_days.pop(chosen_day)] = rain

            else:
                lake[rain] = day
                ans.append(-1)
                
        return ans
                    