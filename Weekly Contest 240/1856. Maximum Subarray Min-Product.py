#Reference:
#https://leetcode.com/problems/maximum-subarray-min-product/discuss/1198718/JavaPython-Stack-keeps-index-of-elements-less-than-numsi-O(N) by hiepit

class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        #main idea:
        #in each element in nums, treat the elem as min
        #find left and right bound, which indicates the sub nums to the left, sub nums to the right, given that the elem as the min
        #left bound is the left most index that fulfill the above condition, vice versa as right bound.
        #calculate the max for each elem, using the leftrightbound.
        
        n = len(nums)
        left_bound, right_bound = [0] * n, [0] * n
        
        #left
        st = []
        for i in range(0, n):
            while st and nums[st[-1]] >= nums[i]:  #pop all elements in stack that >= nums[i], inside stack only <nums[i] will be stored.
                st.pop() #
            if len(st) > 0:
                left_bound[i] = st[-1] + 1 #then the st[-1] will become the smallest index of the nums[i], +1 will become the left bound.
            else:
                left_bound[i] = 0
            st.append(i)
        
        #right
        st = []
        for i in range(n-1, -1, -1):
            while st and nums[st[-1]] >= nums[i]:  #pop all elements in stack that >= nums[i], inside stack only <nums[i] will be stored.
                st.pop() 
            if len(st) > 0:
                right_bound[i] = st[-1] - 1 #then the st[-1] will become the smallest index of the nums[i], -1 will become the right bound.
            else:
                right_bound[i] = n-1 #most right
            st.append(i)
            
        #use prefix sum to track
        presum= [0] * (n+1)

        for i in range(len(nums)):
            presum[i+1] = presum[i] + nums[i]
            
        def get_sum(left,right): #get the sum of the sub nums, right inclusive
            return presum[right+1] - presum[left] 
        
        ans = 0
        for i in range(len(nums)):
            ans = max(ans, nums[i]* get_sum(left_bound[i], right_bound[i]))
        
        return ans %(10**9 + 7)