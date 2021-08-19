#First Attempt: Time limit

from heapq import *
class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        #nums1 always > nums2
        
        if sum(nums1) < sum(nums2):
            temp =nums1
            nums1 = nums2
            nums2 = temp
        
        if len(nums1) > len(nums2)*6:
            return -1
        
        nums1 = [-i for i in nums1]
        
        heapify(nums1)
        heapify(nums2)
        
        operation_count = 0
        while abs(sum(nums1)) > sum(nums2):
            
            #get the smallest to have highest efficiency
            
            if abs(nums1[0])-1 >= 6-nums2[0]: #if nums1 more efficient
                #reduce nums1
                heapreplace(nums1, -1)
            else: #if nums2 more efficient
                #increase nums2
                heapreplace(nums2, 6)
            
            operation_count+=1
            
        return operation_count
        

#Second attempt: 
#Reference: https://leetcode.com/problems/equal-sum-arrays-with-minimum-number-of-operations/discuss/1085786/JavaPython-3-2-Greedy-codes%3A-sort-and-count-w-brief-explanation-and-analysis by rock
from collections import Counter
class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        #nums1 always > nums2
        
        if sum(nums1) < sum(nums2):
            temp =nums1
            nums1 = nums2
            nums2 = temp
        
        if len(nums1) > len(nums2)*6:
            return -1
        
        a = [i-1 for i in nums1] #how much i can sub to each nums1
        b = [6-i for i in nums2] #how much i can add to each nums2
        
        available_operation = Counter(a+b)
    
        operation_count = 0
        #reduce start from 5, to 4, 3,2,1
        j = 5
        s_num1 = sum(nums1)
        s_num2 = sum(nums2)
        while s_num1 > s_num2:
            
            while available_operation[j] == 0:#next num.
                j-=1
                
            available_operation[j] -=1
            s_num1 -= j
            
            operation_count+=1
            
        return operation_count
