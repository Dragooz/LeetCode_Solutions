#Reference: https://leetcode.com/problems/splitting-a-string-into-descending-consecutive-values/discuss/1186813/C%2B%2B-Python-Recursive-Backtracking-solution-explained-w-Comments! 
#by archit91

class Solution:
    def splitString(self, s: str) -> bool:
        #main idea:
        #for each split: (1,2,3,4...)
            #for each possible split(1 with 1,2,3..., 2 with 1,2,3...)
            #check if split == prev -1, if no proceed next split
            #if yes, proceed next round split
        
        #current string index, current split length, previous val, how many times splitted.
        def dfs(s_index, split_length, prev, split_times): 
            if s_index == len(s) and split_times >= 2: #condition to return true
                return True
            
            while s_index + split_length <= len(s): #the index still in range
                cur = int(s[s_index:s_index+split_length])
                split_length += 1
                
                if prev!= -1 and cur != prev-1: #if the condition not met, and not prev=-1,continue splitting.
                    continue #this means that if prev == -1 or cur == prev-1, then it will not execute this
                
                # to reach here, it means that if prev == -1 or cur == prev-1,
                if dfs(s_index+split_length-1, 1, cur, split_times+1):#if reach here, means it is equal
                    return True
            
            return False
        
        return dfs(0, 1, -1, 0)
            