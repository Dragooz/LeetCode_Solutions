#Reference: https://leetcode.com/problems/restore-the-array-from-adjacent-pairs/discuss/1043117/Python3-Graph-%2B-DFS-or-easy-to-understand by SonicM

from collections import defaultdict
class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)
        
        for a,b in adjacentPairs:
            graph[a].append(b)
            graph[b].append(a)
            
        for g, v in graph.items():
            if len(v) ==1:
                start = g
                break
                
        seen = set()
        ans = []
        
        def dp(num):
            seen.add(num)
            ans.append(num)
            for next_num in graph[num]:
                if next_num not in seen:
                    dp(next_num)
                
            return ans
        
        return dp(start)
            
            
        
        
        
            