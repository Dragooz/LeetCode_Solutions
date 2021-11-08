#https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/discuss/660632/Kt-Js-Py3-Cpp-Sliding-Window-Seen-Strings

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        
        seen = set()
        
        q = deque()
        
        for char in s:
            q.append(char)
            
            if len(q) == k:
                seen.add(''.join(q))
                q.popleft()
            
        return len(seen) == 1 << k