class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        
        #main idea:
        #sort the nums list
        #map each sorted with 0, 1, 2,3... etc
        #get the sum
        
        nums.sort()
        ans = [0]
        
        i = 0
        for num_1, num_2 in zip(nums[:-1], nums[1:]):
            if num_1 == num_2:
                ans.append(i)
            else: #not equal
                i+=1
                ans.append(i)

        return sum(ans)
        