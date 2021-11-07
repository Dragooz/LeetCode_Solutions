class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        
        vowel = ['a', 'e', 'i', 'o', 'u']
        def check(word):
            temp = set()
            for char in word:
                temp.add(char)
                if char not in vowel:
                    return False
            
            if len(temp) != 5:
                return False
                
            return True
        
        ans = 0
        n = len(word)
        
        for i in range(n-4):
            window = 5
            while window <= n:
                checking_w = word[i:window]
                if check(checking_w):
                    ans+=1
                window+=1
                
        return ans
                
            
            