class Solution:
    def minOperations(self, s: str) -> int:
        
        n = len(s)
        
        ans1 = ''
        ans2 = ''
        
        for i in range(n):
            if i %2 == 0:
                ans1 += '1'
                ans2 += '0'
            else:
                ans1 += '0'
                ans2 += '1'
        
        op1 = 0
        op2 = 0

        for i in range(n):
            if s[i] != ans1[i]:
                op1 +=1
            if s[i] != ans2[i]:
                op2 +=1
                
        return min(op1, op2)
        