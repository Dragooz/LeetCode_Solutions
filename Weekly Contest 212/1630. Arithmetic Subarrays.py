class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        
        ans= []
        
        for left, right in zip(l, r):
            num = sorted(nums[left:right+1])
            num = set( [num[i] - num[i-1] for i in range(1, len(num))] )
            
            # print(num)
            if len(num) == 1:
                ans.append(True)
            else:
                ans.append(False)
                
        return ans
                    
                
            
        