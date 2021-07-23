#reference:
#https://leetcode.com/problems/unique-binary-search-trees/discuss/31666/DP-Solution-in-6-lines-with-explanation.-F(i-n)-G(i-1)-*-G(n-i) by liaison

class Solution:
    def numTrees(self, n: int) -> int:
        
        #G(n) = dp(1, n) +dp(2, n).. + dp(n,n) #ans
        #G(0) = G(1) = 1 #empty tree count as tree too
        #dp(i, n) = G(i-1) * G(n-i)
        #hence sub 3 into 1:
        #G(n) = G(0) * G(n-1) + G(1) * G(n-2) +...+ G(n-1) * G(0) 
        #the n here is j in the code
        
        g = [1, 1] + [0]*(n-1) #g(0) and g(1)
            
        for i in range(2, n+1):
            for j in range(1, i+1):
                g[i] += g[j-1] * g[i-j] #G(n) += G(0,1,2...i) * G(n-1, n-2...0)
            
            
        return g[n]