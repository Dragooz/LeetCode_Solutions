#First: Reference: https://leetcode.com/problems/the-number-of-weak-characters-in-the-game/discuss/1445192/Python-sort-%2B-greedy-explained

from collections import defaultdict

class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        
        properties.sort()
        groups = defaultdict(list)
        
        for a,b in properties:
            groups[a].append(b)
            
        ans = 0
        max_def = 0
        
        for group in list(groups.keys())[::-1]:
            
            for def_ in groups[group]: #in this loop, atk is confirm higher.
                if def_ < max_def: #first loop, group has highest atk, so no need to append to ans
                    ans +=1
                    
            max_def = max(max_def, *[i for i in groups[group]]) #update max def with max atk
                
                        
        return ans

#Second: Reference: https://leetcode.com/problems/the-number-of-weak-characters-in-the-game/discuss/1445198/Python-Sort

from collections import defaultdict

class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        
        properties.sort(key=lambda x: (-x[0],x[1])) #sort by attack in descending first, then sort by def in ascending to avoid ans+1
        
        ans = 0
        curr_max = 0
        
        print(properties)
        
        for _, d in properties: #def only
            if d < curr_max:
                ans += 1
            else:
                curr_max = d
        return ans
