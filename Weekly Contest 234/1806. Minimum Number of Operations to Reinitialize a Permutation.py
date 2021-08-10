class Solution:
    def reinitializePermutation(self, n: int) -> int:
        perm_ori = [i for i in range(n)]
        perm = [i for i in range(n)]
        temp_perm = [0] * n
        
        count = 0

        while temp_perm != perm_ori:
            for i in range(n):
                if i % 2 == 0:
                    temp_perm[i] = perm[i//2]
                else:
                    temp_perm[i] = perm[(n//2)+ ((i-1)//2)]
            
            perm = temp_perm.copy()
            count+=1
            
        return count