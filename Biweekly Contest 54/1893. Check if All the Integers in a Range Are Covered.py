class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        #main idea
        #1. turn the range of left and right to a list of number
        #2. if element of the list in the range: 
            #remove the element.
        #3. repeat until ranges> right or list is empty
        
        num_list = [ i for i in range(left, right+1)]
    
        for l, r in ranges:
            if num_list[0] > r or l > num_list[-1]: #not in the range
                continue
            else: #in range
                for i in range(l, r+1):
                    if i in num_list:
                        num_list.remove(i)
                        
            if num_list == []:
                return True
            
        return False