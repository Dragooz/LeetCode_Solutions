class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        
        count = Counter(set(nums1))
        count.update(set(nums2))
        count.update(set(nums3))
        
        ans = []
        for k, v in count.most_common():
            if v >= 2:
                ans.append(k)
                
        return ans
        