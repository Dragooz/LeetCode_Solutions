#Reference: https://leetcode.com/problems/maximal-network-rank/discuss/888983/Clean-Python-3-hashmap-O(N2)

import collections

class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        
        graph = collections.defaultdict(set)
        
        for a,b in roads:
            graph[a].add(b)
            graph[b].add(a)
        
        ans = 0
        
        for i in range(n):
            for j in range(i+1, n):
                ans = max(ans, len(graph[i]) + len(graph[j]) - (i in graph[j]) ) #if duplicate then remove 1
        
        return ans
        
        