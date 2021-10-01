class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        
        nnums = []
        
        for i in range(len(nums)):
            temp = 0
            for j in range(i, len(nums)):
                temp += nums[j]
                # heappush(nnums,temp)
                nnums.append(temp)
                
        nnums.sort()
        # print(nnums)
        return sum(nnums[left-1:right]) % (10**9 +7)
            