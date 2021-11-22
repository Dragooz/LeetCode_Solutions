class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        
        words.sort(key=len)
        
        ans = []
        
        for i in range(len(words)-1):
            for j in range(i+1, len(words)):
                if words[i] == words[j] or words[i] in words[j]:
                    ans.append(words[i])
                    break
        
        return ans
                
                    
        
        