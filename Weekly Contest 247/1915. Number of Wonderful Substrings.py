'''
Reference:
https://leetcode.com/problems/number-of-wonderful-substrings/discuss/1299552/JavaC%2B%2BPython-Bit-Mask-%2B-Prefix by lee215
https://leetcode.com/problems/number-of-wonderful-substrings/discuss/1301408/Bitmask-with-pictures-or-Python-or-O(N) by c2hlbGRvbg
https://stackoverflow.com/questions/31575691/what-is-a-bitmask-and-a-mask
https://data-flair.training/blogs/python-operator/

Add-on: 
A prefix is the beginning letter of a word or group of words. - Example: The word “unhappy” consists of the prefix “un."
A suffix is a letter or group of letters added to the end of a word. - Example: Suffix ‘-ly’ is added to ‘quick’ to form ‘quickly’.

'''

class Solution(object):
    def wonderfulSubstrings(self, word):
        """
        :type word: str
        :rtype: int
        """

        #2^10(10 characters), parity for the 10 digits (0-9)
        #1 is because single character is considered as wonderful string too (act as base case)
        count = [1] + [0] * 1023 
        
        #using bitmask
        cur_mask = 0 #keep adding words using XOR
        
        ans = 0 #number of wonderful string
        
        for character in word: #loop through characters
            index = ord(character) - ord('a')
            cur_mask = cur_mask ^ (1 << index) #modifying the mask
            
            #count all even combination
            ans = ans + count[cur_mask] 
            
            #count all even combination with an odd
            #by flipping each bit in the mask
            ans = ans + sum([count[ cur_mask ^ (1 << (i))] for i in range(10)])
            
            #update count dictionary
            count[cur_mask] +=1
            
        return ans