class Solution:
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        ans_groups = []
        
        i=0
        for group in groups:
            gn = len(group)

            while i < len(nums) - gn +1:
                # print(nums[i:i+gn])
                if group == nums[i:i+gn]:
                    ans_groups.append(group)
                    nums = nums[:i] + nums[i+gn:]
                    break
                i+=1

        # print(ans_groups)
        # print(groups)
        if ans_groups == groups:
            return True
        else:
            return False