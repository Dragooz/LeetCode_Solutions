class Solution:
    def minInsertions(self, s: str) -> int:
        s = [i for i in s]
        stack = deque()
        op = 0
        
        while s:
            
            if s[0] == '(':
                stack.append(s.pop(0))
                continue
            else: # = ')'
                if stack and stack[-1] == '(': # ())
                    stack.pop()
                    s.pop(0)
                    if len(s) >= 1 and s[0] == ')':
                        s.pop(0)
                    else:
                        op+=1
                else: #both not exist
                    op+=1 #'('
                    s.pop(0) #')'
                    if len(s) >= 1 and s[0] == ')':
                        s.pop(0)
                    else:
                        op+=1

        return op + (len(stack) *2)