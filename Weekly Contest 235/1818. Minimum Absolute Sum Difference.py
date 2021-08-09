#first attempt failed
class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        
        temp_storage = []
        while True:
            diff = [abs(i-j) for i, j in zip(nums1, nums2)]
            if diff == []:
                return 0
            max_index = [index for index, val in enumerate(diff) if val == max(diff)]
            val = []
            for mi in max_index:
                val.append([min([abs(num-nums2[mi]) for num in nums1]), mi])
            
            val, max_index = min(val)
            
            if val == diff[max_index]: #means no suitable change
                temp_storage.append(diff[max_index])
                nums1.pop(max_index)
                nums2.pop(max_index)
            else:
                diff[max_index] = val
                break
        
        return (sum(diff) + sum(temp_storage)) %(10**9 +7)

#second attempt: Reference: https://leetcode.com/problems/minimum-absolute-sum-difference/discuss/1141382/Clean-Python-3-binary-search by lenchen1112

class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        
        diff_sum, diff = 0, []
        
        for i in range(len(nums1)):
            absdiff = abs(nums1[i] - nums2[i])
            diff.append(absdiff)
            diff_sum += absdiff
            
        nums1.sort()
        ans = float('inf')
        for num2, dif in zip(nums2, diff):
            index = bisect.bisect_left(nums1, num2) #input the num2 into nums1, where it form ascending, to the most left.
            
            if index>0: #not the most left
                ans = min(ans, diff_sum - dif + (abs(num2- nums1[index-1]))) #the abs part the actually num2 deducting the closest value of num1 (left)
            if index <len(nums1): #double check, now right side
                ans = min(ans, diff_sum - dif + (abs(num2- nums1[index]))) #the abs part the actually num2 deducting the closest value of num1 (right)

        return ans% (10**9 +7)
                
            