class Solution:
    def maxValue(self, n: str, x: int) -> str:
        
        #main idea: 
        #if '-', the job is to minimize the number
        #if '+', the job is to maximize the number
        #to minimize, iterating from left to right, when the digit>x, plug x to the left of the digit
        #to maximize, iterating from left to right, when x>the digit, plug x to the left of the digit
        
        sign = True
        
        if n[0] == '-': #negative
            n = n[1:]
            sign=False
            
        if sign: #positive
            ans = 0
            for index, digit in enumerate(n):
                if x > int(digit):
                    ans = n[0:index] + str(x) + n[index:]
                    break
            
            if ans==0:
                ans = n + str(x)
                
        else: #negative
            ans = 0
            for index, digit in enumerate(n):
                if x < int(digit):
                    ans = '-' + n[0:index] + str(x) + n[index:]
                    break
            
            if ans==0:
                ans = '-' + n + str(x)
        
        return ans
            
            