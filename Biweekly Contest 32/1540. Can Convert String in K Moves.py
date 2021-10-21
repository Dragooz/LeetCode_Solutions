#Reference: https://leetcode.com/problems/can-convert-string-in-k-moves/discuss/779938/Python-O(n)-Explained

class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        
        if len(s) != len(t):
            return False
        
        convert = 0
        diff = defaultdict(int)
        
        for a, b in zip(s, t):
            
            op = (ord(b) - ord(a)) % 26
            if op == 0:
                continue
            
            if op > k:
                return False
            
            diff[op] += 1
            
            if ((diff[op]-1) *26) + op > k:
                return False
            
        return True