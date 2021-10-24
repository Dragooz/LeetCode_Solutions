class Solution:
    def countValidWords(self, sentence: str) -> int:
        
        ans = 0 
        punc = ['!', '.', ',']
        
        for s in sentence.split(' '):
            if any(i.isdigit() for i in s) or any(i in punc for i in s[:-1]) or s=='' or s.lower() != s:
                continue
            else:
                if '-' in s:
                    temp = 0
                    for sen in s:
                        if sen == '-':
                            temp+=1
                    
                    if temp>1:
                        continue
                    
                    index = s.index('-')
                    
                    if index==(len(s)-1) or index==0:
                        continue
                    else:
                        if s[index-1].isalpha() and s[index+1].isalpha():
                            ans+=1
                        else:
                            continue
                else:
                    ans+=1
        
        return ans
        
        