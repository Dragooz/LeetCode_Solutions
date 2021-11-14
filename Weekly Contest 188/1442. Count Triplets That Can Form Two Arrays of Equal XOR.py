#Reference: https://leetcode.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor/discuss/623747/JavaC%2B%2BPython-One-Pass-O(N4)-to-O(N)

class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        
        arr.insert(0,0) #at index 0, insert 0
        ans = 0
        
        for i in range(len(arr)-1):
            arr[i+1] = arr[i+1] ^ arr[i]
            
            
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                if arr[i] == arr[j]: # a = b, a^a = a^b, a^b == 0 
                    ans += j-i-1
                    
        return ans