#Reference: https://leetcode.com/problems/split-a-string-into-the-max-number-of-unique-substrings/discuss/855071/Python3-backtracking

class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        #dfs
        def fn(i, seen=set()):
            ans = 0
            if i < len(s): #check whether it exceed s
                for ii in range(i+1, len(s)+1): #every possible split
                    if s[i:ii] not in seen:
                        seen.add(s[i:ii]) 
                        ans = max(ans, 1+fn(ii, seen)) #if seen then only update
                        seen.remove(s[i:ii]) #backtrack by removing
            
            return ans
        
        return fn(0)