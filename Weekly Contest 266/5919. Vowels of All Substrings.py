class Solution:
    def countVowels(self, word: str) -> int:
        
        vowel = ['a', 'e', 'i', 'o', 'u']
        ans = 0
        vowel_num = 0
        n = len(word)
        record = [0] * n 
        
        for index, char in enumerate(word):
            if char in vowel:
                vowel_num +=1
            record[index] = vowel_num
        
        acc = list(accumulate(record))
        # print(record)
        # print(acc)
        
        for i in range(n):
            if i == 0:
                ans += (record[i] * (i+1))
            else:
                ans += (record[i] * (i+1)) - acc[i-1]
                
        return ans