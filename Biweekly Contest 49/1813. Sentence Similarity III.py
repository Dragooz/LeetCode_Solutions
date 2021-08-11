class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        #main idea: sentence 2 always > sentence 1
        #pop from left and right
        #if done, means its valid
        
        if len(sentence1) > len(sentence2): #swap
            temp = sentence1
            sentence1 = sentence2
            sentence2 = temp
        
        if sentence1 == sentence2:
            return True
        
        sentence1 = sentence1.split(' ')
        sentence2 = sentence2.split(' ')
       
        while sentence1:
            if sentence1[0] == sentence2[0]:
                sentence1.pop(0)
                sentence2.pop(0)
            elif sentence1[-1] == sentence2[-1]:
                sentence1.pop(-1)
                sentence2.pop(-1)
            else:
                break
        
        return sentence1 == []