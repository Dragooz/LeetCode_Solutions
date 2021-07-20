class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        
        #main idea:
        #loop through the nums
        #if num[1] > num[0], proceed.
        #if num[1] < num[0], split into two list, then loop through those 2 again
        
        nl = len(nums)
        if nl <=2: return True
        
        removed = False
        temp = nums[0]
        first_list = None
        for i in range(1, nl):
            if nums[i] > temp: #keep going
                temp = nums[i]
                continue
                
            else: #met a smaller num
                #splitted into two 
                first_list = nums[:i] + nums[i+1:]
                second_list = nums[:i-1] + nums[i:]
                break
        
        if first_list != None:
            pass_ = [True, True]
            for index, list_ in enumerate([first_list, second_list]):
                temp = list_[0]
                for j in range(1, len(list_)):
                    if list_[j] >temp:
                        temp = list_[j]
                        continue
                    else:
                        pass_[index] = False
                        break
                        
            if pass_[0] == True or pass_[1] == True:
                return True
            else:
                return False
            
        return True #if everything is okay