#Reference: https://leetcode.com/problems/shortest-subarray-to-be-removed-to-make-array-sorted/discuss/830699/Python-Two-Pointers-Approach-with-Explanation

class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        
        
        n = len(arr)
        l, r = 0, len(arr)-1
        
        while l < r and arr[l] <= arr[l+1]:
            l+=1
            
        if l == len(arr)-1:
            return 0 
            
        while r>0 and arr[r] >= arr[r-1]:
            r-=1
            
        ans = min(n-l-1, r) #only left, only right
        
        #merging
        for i in range(l+1):
            if arr[i] <= arr[r]:
                ans = min(ans, r-i-1) #0-indexed
            elif r < n-1: #increase threshold
                r+=1
            else:
                break
            
        return ans
        
        
            
        