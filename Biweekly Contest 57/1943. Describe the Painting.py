#Reference: https://leetcode.com/problems/describe-the-painting/discuss/1359717/Python-Easy-solution-in-O(n*logn)-with-detailed-explanation by fishballLin

import collections
class Solution:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        
        map_ = collections.defaultdict(int)
        
        for s, e, c in segments:
            map_[s] += c
            map_[e] -= c
            
        res = []
        prev, color = None, 0 #prev= coordinates before, color = the color value
        
        for coor in sorted(map_): 
            if prev != None and color != 0:
                res.append([prev, coor, color])
                
            prev = coor
            color += map_[coor]
            
        return res