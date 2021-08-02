class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        #if the largest val in milestones < the sum of milestones except the largest val: means it can complete all milestones.
        #hence, return the total of the milestones.
        #else, then it will be able to complete only the sum of milestones except the largest val, multiplied by 2, plus 1 (as it started
        #from the largest val)
        
        if len(milestones) <= 1:
            return 1
        
        milestones.sort()
        
        max_ = milestones.pop(-1)
        sum_ = sum(milestones)

        if sum_ >= max_ :
            return sum_ + max_
        else:
            return (sum_)*2 + 1