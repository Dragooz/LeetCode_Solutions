#Reference: https://leetcode.com/problems/check-if-word-can-be-placed-in-crossword/discuss/1486285/Python-3-working-with-strings

class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        
        words = [word, word[::-1]]
        n = len(word)
        
        for B in board, zip(*board): #check hori, check verti
            
            for row in B:
                q = ''.join(row).split('#')

                for w in words:
                    for s in q:
                        if len(s) == n:
                            if all(s[i] == w[i] or s[i] == ' ' for i in range(n)):
                                return True
                            
        return False
                            