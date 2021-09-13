from collections import Counter

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        count = Counter(nums)
        ans = 0

        for index, (key, val) in enumerate(count.most_common()):
            if count[key] >0 and count[k-key] >0: #pairs exist
                if key != k-key:  #diff num
                    min_ = min(count[key], count[k-key])
                    ans += min_
                    count[key] -= min_
                    count[k-key] -= min_
                else: #same num
                    
                    ans += count[key]// 2
                    count[key] -= (count[key]//2 *2)
                
        return ans
            