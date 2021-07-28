#first try, time exceed

class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        #main idea:
        #check from behind, once found, record the index in nums1. 
        #then, only need to check <index in nums1
        
        max_dist = 0
        
        num1_l = len(nums1)
        num2_l = len(nums2)
        
        for j in range(num2_l-1, -1, -1): #start from behind till 0
            for i in range(num1_l):
                
                if j-i < max_dist:
                    break
                
                if nums2[j] >= nums1[i] and j>=i: #found a match
                    max_dist = max(j-i, max_dist)
                    
                    
        
        return max_dist
        
#second try
#Reference from https://leetcode.com/problems/maximum-distance-between-a-pair-of-values/discuss/1198733/JavaC%2B%2BPython-2-Pointers-3-Solutions lee215

class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        #main idea: nums1 cannot > nums2
        #loop through nums2
        #if nums1[i] > nums2[i] --> i+=1 skip num 1
        #else, record the max
        ans = 0
        i = 0
        for j, num2 in enumerate(nums2):
            while len(nums1) > i and nums1[i] > num2: #invalid
                i+=1 #go forwards in nums1 as it is already invalid

            if i == len(nums1):
                break
            ans = max(ans, j-i) #update ans if valid
            
        return ans