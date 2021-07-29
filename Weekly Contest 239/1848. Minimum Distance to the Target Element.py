class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        
        index_list= [index for index, num in enumerate (nums) if num ==target]
        return min([abs(i-start) for i in index_list])