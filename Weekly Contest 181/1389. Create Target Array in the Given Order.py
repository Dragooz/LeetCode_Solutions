class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        ans = deque()
        
        for i, num in zip(nums, index):
            ans.insert(num, i)
            
        return ans