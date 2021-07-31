#Reference: https://leetcode.com/problems/longest-substring-of-all-vowels-in-order/discuss/1175189/Best-C%2B%2B-Solution by 6cdh

class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        #main idea:
        #if the word_prev > word_cur: reset
        #else, increment
        #count of unique char ==5, means all available, update length
        
        unique = 1
        sub_len = 1
        ans = 0
        word_prev = word[0]
        
        for i in range(1, len(word)):
            if word_prev <= word[i]: #valid
                sub_len +=1
                if word_prev != word[i]:
                    unique +=1
            elif word_prev > word[i]:#invalid, reset
                unique = 1
                sub_len = 1
            
            if unique == 5: #aeiou exist
                ans = max(ans, sub_len)
                
            word_prev = word[i]
            
        return ans