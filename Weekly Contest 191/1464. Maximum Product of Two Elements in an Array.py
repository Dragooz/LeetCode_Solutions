class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums = [-i for i in nums]
        heapify(nums)

        a = -heappop(nums) -1
        b = -heappop(nums) -1
        
        return a*b 