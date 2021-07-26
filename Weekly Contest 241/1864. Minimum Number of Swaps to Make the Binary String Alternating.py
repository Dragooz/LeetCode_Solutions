class Solution:
    def minSwaps(self, s: str) -> int:
        #get two possible answer list -> 10101, 01010
        #compare the number of swaps
        
        sl = len(s)
        
        one_ans = ''
        two_ans = ''
        zero = 0
        one = 0
        
        for i, char in enumerate(s):
            if i%2 == 0:
                one_ans += '1'
                two_ans += '0'
            else:
                two_ans += '1'
                one_ans += '0'
            
            if char == '0':
                zero+=1
            else:
                one+=1
        # print(zero, one)
        if abs(zero-one) > 1:
            return -1
                
#         print(one_ans)
#         print(two_ans)
            
        ans_1 = 0
        ans_2 = 0
        
        for index in range(sl):
            if s[index] != one_ans[index]:
                ans_1 +=1
            if s[index] != two_ans[index]:
                ans_2 +=1
        
        if ans_1%2 == 0 and ans_2%2 == 0:
            return min(int(ans_1/2), int(ans_2/2))
        elif ans_1%2 == 0:
            return int(ans_1/2)
        elif ans_2%2 == 0:
            return int(ans_2/2)
        else:
            return -1