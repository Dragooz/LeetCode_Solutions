#Reference: https://leetcode.com/problems/split-two-strings-to-make-palindrome/discuss/888967/JavaC%2B%2BPython-Greedy-Solution-O(1)-Space

class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        
        #either a pre + b suf or b pre + a suf
        
        i, j = 0, len(b) -1
        
        while i<j and a[i] == b[j]: #to get the middle, that need to further check whether it is palindrome or not.
            i+=1
            j-=1
        
        s1, s2 = a[i:j+1], b[i:j+1]
        
        i, j = 0, len(a) -1
        while i<j and b[i] == a[j]:
            i+=1
            j-=1
            
        s3, s4 = b[i:j+1], a[i: j+1]
        
        return any(s == s[::-1] for s in [s1,s2,s3,s4])