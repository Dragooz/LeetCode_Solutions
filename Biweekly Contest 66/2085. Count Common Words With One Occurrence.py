class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        
        c = defaultdict(int)
        
        for w in words1:
            c[w] +=1 
            
            if c[w] > 1:
                c[w] = -1001 #to prevent
            
        for w in words2:
            if c[w]:
                c[w] += 1
                
        
        return len([i for i in c.keys() if c[i]==2])
    
    
        