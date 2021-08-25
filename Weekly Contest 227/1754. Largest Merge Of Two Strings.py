#Reference: https://leetcode.com/problems/largest-merge-of-two-strings/discuss/1053549/JavaC%2B%2BPython-Easy-Greedy by lee215

class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        
        if word1 >= word2 > '':
            return word1[0] + self.largestMerge(word1[1:], word2)
        elif word2 > word1 > '':
            return word2[0] + self.largestMerge(word1, word2[1:])
        
        return word1 + word2