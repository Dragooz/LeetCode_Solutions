class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        
        ans = 0
        
        for i in range(len(mat)): #row
            for j in range(len(mat[0])): #col
                
                cur = mat[i][j]
                
                if cur == 0:
                    continue
                else:
                    append=True    
                    for k in range(len(mat)):
                        if k != i:
                            if cur == mat[k][j]: #both = 1
                                append=False
                                break
                    
                    for l in range(len(mat[0])):
                        if l != j:
                            if cur == mat[i][l]:
                                append=False
                                break
                    
                    if append:
                        ans+=1
                        
        return ans

#OR

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        
        ans = 0
        trans = list(zip(*mat))
        
        for i in range(len(mat)): #row
            for j in range(len(mat[0])): #col
               
                if mat[i][j] == 1 and sum(mat[i]) == 1 and sum(trans[j]) == 1:
                    ans+=1
                        
        return ans
        
        
        
        