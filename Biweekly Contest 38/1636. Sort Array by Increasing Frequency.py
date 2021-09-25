from collections import Counter

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        
        count = list(Counter(nums).most_common())
        
        count = sorted(count, key=lambda x: [x[1], -x[0]])
            
        ans = []
        
        for val, freq in count:
            for _ in range(freq):
                ans.append(val)
                
        return ans