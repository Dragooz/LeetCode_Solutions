class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        
        nums = []
        seq = []
        for char in word:
            if char.isnumeric():
                seq.append(char)
            else:
                if seq != []:
                    nums.append(int(''.join(seq)))
                seq = []
                
        if seq != []:
            nums.append(int(''.join(seq)))
        
        print(nums)
        return len(set(nums))
                