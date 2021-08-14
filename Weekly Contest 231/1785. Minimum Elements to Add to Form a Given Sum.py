class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        diff = abs(sum(nums) - goal)
        
        # if diff%limit == 0:
        #     return diff//limit
        # else:
        #     return (diff//limit) +1
        
        #replace above with this thinking:
        #diff + (limit-1) --> for example, 5 with limit 3, goal of 10, then the answer is two
        #if follow above, then its 5//3 +1 
        #if follow below, then its (5+3-1)//3 --> it will bring up limit-1 of the diff, make it always ceiling.
        return (diff +(limit-1)) // limit