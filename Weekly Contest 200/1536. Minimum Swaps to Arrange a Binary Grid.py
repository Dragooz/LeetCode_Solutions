#Reference: https://leetcode.com/problems/minimum-swaps-to-arrange-a-binary-grid/discuss/768010/Python-Clean-greedy-solution-with-detailed-explanation-O(N2)

class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        
        def count_zeros(arr):
            ans = 0
            for i in range(n-1, -1, -1):
                if arr[i] == 0:
                    ans+=1
                else:
                    break
                    
            return ans
                
        arr = [count_zeros(i) for i in grid]
        ans = 0
        
        for i in range(n):
            target = n-i-1 #trailing zero that it must have
            
            if arr[i] >= target:
                continue
            flag = False #possible to find suitable row
            for j in range(i+1, n):
                
                if arr[j] >= target:
                    flag = True
                    ans += j-i #number of swap required.
                    arr[i+1:j+1] = arr[i:j] #overwrite 
                    break
            
            if not flag:
                return -1 
            
        return ans                
                    
                
            
        
        