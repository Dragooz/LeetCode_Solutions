#Reference: https://leetcode.com/problems/frequency-of-the-most-frequent-element/discuss/1175090/JavaC%2B%2BPython-Sliding-Window by lee215

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        #sort the nums
        #sliding windows
        #if size of windows* max of elem in each windows < sum of nums + k : valid.
        #if not valid, remove the first element. since its sorted, this can be done.
        #return the size.
        
        nums.sort()
        
        sum_ = k
        i= 0
        for j in range(len(nums)):
            
            sum_ += nums[j]
            
            if (j-i+1) * nums[j] > sum_: #invalid
                sum_ -= nums[i] #remove the first element from the window
                i+=1 #increment.
                
        return j-i+1 #size is the answer.