#Reference: https://leetcode.com/problems/count-substrings-that-differ-by-one-character/discuss/917701/C%2B%2BJavaPython3-O(n-3)-greater-O(n-2)

class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        
        n, m = len(s), len(t)
        res = 0
        
        for i in range(n):
            for j in range(m):
                pos, miss = 0, 0
                
                while pos + i < n and pos+j < m and miss <2 :
                    miss += s[pos+i] != t[pos+j]
                    res += miss==1
                    pos+=1
                    
        return res
                
                
