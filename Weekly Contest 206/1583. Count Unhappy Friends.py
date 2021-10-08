#Reference: https://leetcode.com/problems/count-unhappy-friends/discuss/844105/Python-Clean-Solution

class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        
        d = {}
        ans=0
        for i, x in pairs: #get closer friends
            d[i] = set(preferences[i][:preferences[i].index(x)])
            d[x] = set(preferences[x][:preferences[x].index(i)])
            
        for i in d:
            for x in d[i]:
                if i in d[x]: #if i appeared in closer list of x
                    ans+=1
                    break

        return ans