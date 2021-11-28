#Attempt 1: Memory Limit error
class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        
        dict_ = defaultdict(list)
        
        for i in reservedSeats:
            if i[1] != 1 and i[1] != 10:
                dict_[i[0]].append(i[1])
        
        ans = 0
        
        for i in range(1, n+1):
            
            cols = [1] * 8
            for val in dict_[i]:
                cols[val-2] = 0

            if sum(cols) == 8:
                ans+=2
            else:
                if sum(cols[0:4]) == 4:
                    ans+=1
                elif sum(cols[2:6]) == 4:
                    ans+=1
                elif sum(cols[4:8]) == 4:
                    ans+=1
                else:
                    pass
                
        return ans
            
#Attempt 2: Reference: https://leetcode.com/problems/cinema-seat-allocation/discuss/552211/Python-Very-concise-solution-using-hash-map

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        
        unique = defaultdict(set)
        
        for i,j in reservedSeats:
            
            if j in [2,3,4,5]:
                unique[i].add(0)
            if j in [4,5,6,7]:
                unique[i].add(1)
            if j in [6,7,8,9]:
                unique[i].add(2)
            
        ans = 2*n #max
        
        for i in unique:
            if len(unique[i]) == 3:
                ans-=2
            elif len(unique[i])>0:
                ans-=1
                
        return ans
            
            
            
            