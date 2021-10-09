class Solution:
    def modifyString(self, s: str) -> str:
        index = 0
        while '?' in s:
            if s[index] == '?':
                if index-1 >= 0:
                    prev = ord(s[index-1])
                else:
                    prev = math.inf
                    
                if index+1 < len(s):
                    next_ = ord(s[index+1])
                else:
                    next_ = math.inf
                
                for i in range(26):
                    char = ord('a') + i
                    print('char:',char)
                    if char != prev and char != next_:
                        s = s.replace('?', chr(char), 1)
                        print(s)
                        break
                        
            index+=1
        return s