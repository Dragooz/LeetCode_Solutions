#Reference: https://leetcode.com/problems/number-of-ways-where-square-of-number-is-equal-to-product-of-two-numbers/discuss/831684/python-solution

class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        
        d1 = defaultdict(int)
        d2 = defaultdict(int)
        
        for i in nums1:
            d1[i*i] += 1
        for i in nums2:
            d2[i*i] += 1
            
        ans = 0
        
        #all possible multiplication in nums1, asa the j < k
        for i in range(len(nums1)-1):
            for j in range(i+1, len(nums1)):
                prod = nums1[i] * nums1[j]
                ans += d2[prod]
                
        #all possible multiplication in nums2, asa the j < k
        for i in range(len(nums2)-1):
            for j in range(i+1, len(nums2)):
                prod = nums2[i] * nums2[j]
                ans += d1[prod]
                
        return ans