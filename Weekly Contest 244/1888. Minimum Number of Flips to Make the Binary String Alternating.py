#reference:
# https://leetcode.com/problems/minimum-number-of-flips-to-make-the-binary-string-alternating/discuss/1253874/C%2B%2B-Solution-sliding-window.-O(N)-Time-O(1)-Space by chejianchao

class Solution:
    def minFlips(self, s: str) -> int:
        
        # sliding windows
        # s = s + s to manipulate each possible combination due to operation 1
        # the final answer is either 010101 or 101010, so we create 2 answers to compare with size of s
        # loop through s and keep track of the number of flipping to suit ans1 and ans2
        # if the loop >= s, which means the windows is already not includes in starting index, 
        # start to revert number of flip operation if have revert earlier
        # if loop > s, which means it has finish the first window, start updating the answer.
        # return the minimum flip
        
        ori_sl = len(s)
        s = s+s
        sl = len(s)
        
        ans1 = '' #101...
        ans2 = '' #010...
        
        for i in range(sl):
            if i%2 == 0:
                ans1 += '1'
                ans2 += '0'
            else:
                ans1 += '0'
                ans2 += '1'
        
        flip_ans = sl +1 #max number of flip, impossible to achieve
        flip_1 = 0
        flip_2 = 0
        
        for index, _ in enumerate(s):
            if s[index] != ans1[index]: 
                flip_1 +=1
                
            if s[index] != ans2[index]:
                flip_2 +=1
                
            if index >= ori_sl: #window starts to ignore first index, starting reverting if flip before.
                if s[index-ori_sl] != ans1[index-ori_sl]: 
                    flip_1 -=1
                    
                if s[index-ori_sl] != ans2[index-ori_sl]:
                    flip_2 -=1
            
            if index >= ori_sl-1: #first window done, keep updating the answer onwards
                flip_ans = min(flip_ans, flip_1, flip_2)
                
        return flip_ans