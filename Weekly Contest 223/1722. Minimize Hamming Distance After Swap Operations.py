#Reference from: https://leetcode.com/problems/minimize-hamming-distance-after-swap-operations/discuss/1009864/Python3-UnionFind

from collections import defaultdict

class UnionFind:
    
    def __init__(self, n): 
        self.root = list(range(n))
    
    def union(self, x, y): 
        self.root[self.find(x)] = self.find(y)
    
    def find(self, x):
        # print('x:', x)
        # print('self.root[x]', self.root[x])
        if x != self.root[x]: 
            # print('not equal!')
            self.root[x] = self.find(self.root[x])
        return self.root[x]


class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        
        uf = UnionFind(len(source))
        for x, y in allowedSwaps: 
            uf.union(x, y)
        
        m = defaultdict(set)  # key is the component, value is the set of indices in same component
        for i in range(len(source)): #find which node connect to which
            m[uf.find(i)].add(i)

        # print(m)
        
        ans=0
        for indices in m.values(): #loop through connected
            A = Counter([source[i] for i in indices]) #indices here means all can interchange
            B = Counter([target[i] for i in indices])
            # print('A:', A)
            # print('B:', B)
            ans += sum((A - B).values()) #so here is just to get the amount of different numbers
            
        return ans