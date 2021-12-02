class Solution:
    def generateTheString(self, n: int) -> str:
        
        if n%2 == 0: #even
            return 'a' * (n-1) + 'b'
        else: #odd
            return 'a' * n
        