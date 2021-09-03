from collections import defaultdict
class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        
        perm_ans = 0
        memo = defaultdict()
        
        for i in range(len(nums)):
            memo_done=False
            ans = [nums[i]]
            j = i
            if memo.get(j, -1) != -1:
                continue
            
            while len(ans) < len(nums):
                j = ans[-1]
                
                if nums[j] in ans:
                    break
                else:
                    ans.append(nums[j])
            
            if not memo_done:
                for char in ans:
                    memo[char] = len(ans)

        return max(memo.values())