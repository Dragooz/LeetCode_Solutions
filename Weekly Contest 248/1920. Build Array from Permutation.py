class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        array_list = []
        for i in range (len(nums)):
            array_list.append(nums[nums[i]])
            
        return array_list
        