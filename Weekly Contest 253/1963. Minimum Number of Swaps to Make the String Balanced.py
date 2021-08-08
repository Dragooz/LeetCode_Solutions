class Solution:
    def minSwaps(self, s: str) -> int:
        s = list(s)
        stack = []
        
        for char in s: #using stack to simplify
            if char == '[':
                stack.append(char)
            else: #']'
                if stack and stack[-1] == '[':
                    stack.pop()
                else:
                    stack.append(char)

        len_ = len(stack)
        
        ans = 0
        while len_ >0: 
            len_ -=4 #each swap can solve 2 pairs of bracket
            ans+=1
        return ans