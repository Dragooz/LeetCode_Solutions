from collections import Counter
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        
        count = Counter(nums)
        
        return sum(key for key, val in count.most_common() if val ==1)
        