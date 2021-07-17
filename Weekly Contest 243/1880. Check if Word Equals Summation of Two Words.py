class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        
        def count(words):
            sum_ = 0
            for index, char in enumerate(words):
                val = int(ord(char) - ord('a'))
                sum_ += val * 10**(len(words) -1 -index)
            return sum_
        
        return (count(firstWord) + count(secondWord)) == count(targetWord)