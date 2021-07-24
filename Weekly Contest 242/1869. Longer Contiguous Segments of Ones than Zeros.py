class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        #main idea:
        #true if 1>0
        
        longest_zero = 0
        longest_one = 0
        
        temp_zero = 0
        temp_one = 0
        
        for num in s:
            if num == '0':
                temp_zero +=1
                temp_one = 0
                
                if longest_zero < temp_zero:
                    longest_zero = temp_zero
                
            else: # '1'
                temp_zero= 0
                temp_one +=1
                
                if longest_one < temp_one:
                    longest_one = temp_one
                    
        return longest_one > longest_zero