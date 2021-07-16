#References:
# https://leetcode.com/problems/maximum-number-of-removable-characters/discuss/1268520/Python-Binary-Search by OysterMax

class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        
        #main idea:
        #go thorugh the removals, then if loop check whether after removing one of the elements in removal, p is still sub of s
        #but too slow, so we implement binary search (that is to start at the middle of the removable list)
        #For example, removal = [3,1,0], then we remove [3,1] from the s and see whether p is still sub of s.
        #if yes, then we proceed to higher k to remove more, else, we go back to remove less.
        
        def is_sub(k):
            remove = set(removable[:k+1]) #set faster than list if need to find object
            i = 0 #i to track string
            j = 0 #j to track sub string
            
            while i<sl and j<pl: #both must be true to loop

                if s[i] == p[j] and i not in remove: #found match, and it is not removed.
                    i += 1
                    j += 1 #increment both
                else: #not found
                    i += 1 #increment i only
                    
            return j == pl #if match, then they are subs.
                
        sl, pl, rl = len(s), len(p), len(removable)
        
        low = 0
        high = rl
        
        while low < high:
            mid = (low+high)//2

            if is_sub(mid): #found match, proceed to remove more
                low = mid + 1
            else: #no match, proceed to remove less
                high = mid 
        
        return low #the number of index can be removed.