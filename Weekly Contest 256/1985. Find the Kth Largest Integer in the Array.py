class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums = sorted(list(map(int, nums)))
        return str(nums[-k])