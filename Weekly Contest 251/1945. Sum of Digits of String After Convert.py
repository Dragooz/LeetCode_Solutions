class Solution:
    def getLucky(self, s: str, k: int) -> int:
        
        s_1 = ''.join( [str(ord(char) - ord('a') + 1) for char in s])

        for _ in range(k):
            s_1 = str(sum([int(i) for i in s_1]))
        
        return int(s_1)