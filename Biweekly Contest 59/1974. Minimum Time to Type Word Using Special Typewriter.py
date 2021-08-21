class Solution:
    def minTimeToType(self, word: str) -> int:
        cur = 'a'
        
        op = 0
        
        for w in word:
            turn_num = abs(ord(w) - ord(cur))
            cur = w
            if turn_num >=14:
                turn_num = 26 - turn_num
            # print('here:',turn_num)
            op += turn_num + 1
           
        return op