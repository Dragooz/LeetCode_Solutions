class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        
        #main idea:
        #record the length of substring, use the concept of slide window.
        #if match, slice
        #repeat

        #from discussion, better to implement KMP algo (Knuth–Morris–Pratt algorithm) that can helps to find substring
        
        ssl = len(part)
        i = 0
        while True:
            if s[i:i+ssl] == part:
                s = s[:i] + s[i+ssl:]
                i= 0
                continue
                
            if i+ssl > len(s):
                break
                
            i+=1
            
        return s