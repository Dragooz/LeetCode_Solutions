#Reference: https://leetcode.com/problems/maximum-length-of-subarray-with-positive-product/discuss/819329/Python3GoJava-Dynamic-Programming-O(N)-time-O(1)-space

class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
    
        pos = int(nums[0] > 0) #longest end with positive
        neg = int(nums[0] < 0) #longest end with negative
        
        ans = pos
        for i in range(1, len(nums)):
            
            if nums[i] > 0 :
                pos += 1
                if neg > 0: #if end with neg exist:
                    neg+=1
                    
            elif nums[i] < 0 :
                
                temp_neg = pos + 1
                if neg>0: #exist, then can flip
                    temp_pos = neg + 1
                else:
                    temp_pos = 0
                
                pos, neg = temp_pos, temp_neg

            else:
                pos, neg = 0, 0
            
            ans = max(ans, pos)
        
        return ans