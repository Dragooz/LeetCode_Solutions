#References:
#https://leetcode.com/problems/merge-triplets-to-form-target-triplet/discuss/1268471/Python-Why-greedy-works-here-explained by DBabichev and fishballLin

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        #idea: if target's element < list elements, means can't use, forfeit the triplet (AND condition is able to achieve this)
        #check if target's element == list elements.
        #if all match, return True, else False
        
        trip_l = len(triplets)
        
        a,b,c = 0, 0, 0 #answer
        
        for x, y, z in triplets:
            if x<=target[0] and y<=target[1] and z<=target[2]:
                a = max(a, x)
                b = max(b, y)
                c = max(c, z)
            
        return [a,b,c] == target