class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        ans = 0
        
        stack1 = []
        length1 = 0 
        temp1 = 0
        
        stack2 = []
        length2 = 0 
        temp2 = 0
        
        for char in answerKey:
            
            #Calculate T
            length1+=1
            if char == 'F':
                stack1.append(temp1)
                temp1 = 0
            else:
                temp1 +=1
                
            if len(stack1) > k:
                length1 -= stack1.pop(0) + 1
                
            # print(stack1)
            # print(length1)
                
            #Calculate F
            length2+=1
            if char == 'T':
                stack2.append(temp2)
                temp2 = 0
            else:
                temp2 += 1
                
            if len(stack2) > k:
                length2 -= stack2.pop(0) + 1
                
            # print(stack2)
            # print(length2)
                
            ans = max(ans, length1, length2)
                
        return ans