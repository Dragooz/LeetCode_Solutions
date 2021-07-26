#Reference:
#https://leetcode.com/problems/finding-pairs-with-a-certain-sum/discuss/1211065/JavaPython-Two-sum-problem-using-HashMap-Clean-and-Concise by hiepit

from collections import Counter

class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.nums_freq = Counter(nums2) #keep track of how many count of each num in nums2

    def add(self, index: int, val: int) -> None: #when adding a val into the element of nums2, update nums_freq too
        self.nums_freq[self.nums2[index]] -=1
        self.nums2[index] += val
        self.nums_freq[self.nums2[index]] +=1
    
    def count(self, tot: int) -> int: # nums_freq[tot - element in nums1] will be the answer
        ans = 0 
        for num in self.nums1:
            ans += self.nums_freq[tot - num]
            
        return ans

# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)