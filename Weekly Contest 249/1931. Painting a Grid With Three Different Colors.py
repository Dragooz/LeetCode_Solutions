#Reference:
#https://leetcode.com/problems/painting-a-grid-with-three-different-colors/discuss/1330193/Python-Straight-forward-solution by vbshubham


from functools import cache
from itertools import product

class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        mod = 10**9 +7
        
        def check_adj(combi, combi_1):
            return all(a != b for a, b in zip(combi, combi_1)) #return false if there's same adj
        
        #idea here is:
        #get the possible combination of columns, given m, that first, don't have adj colour = same
        #here it check the vertical clash
        #this return a list of columns
        states = {''.join(combi) for combi in product('RGB', repeat=m) if check_adj(combi, combi[1:])} #get combi that don't have same adj

        
        #second step here is to create the possible step after the next columns
        #that doesn't clash as well.
        #here it check the adj clash 
        #this return columns with possible next columns
        adj = {}
        for state in states:
            adj[state] = [next_state for next_state in states if check_adj(state, next_state)]
        
        #create a dp function
        @cache #caching to retrieve faster + reduce calculation time
        def dp(prev_state, N):
            if N ==0: #base case, when it reach the end of N
                return 1
            
            #else, continue looping, return the sum, which is possible combination along the way.
            return sum(dp(next_state, N-1) for next_state in adj[prev_state]) % mod

        #execute dp
        return sum(dp(state, n-1) for state in states) % mod