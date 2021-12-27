class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        
        biggest_a = 0
        
        for index, char in enumerate(palindrome): #forward pass
            if char == 'a':
                biggest_a = index
                
            ans = palindrome
            temp = char
            for i in range(ord('a'), ord(temp)+1):
                ans = ans[:index] + chr(i) + ans[index+1:]
                if ans != ans[::-1]:
                    return ans
        
        if biggest_a != 0:
            return ans[:biggest_a] + 'b' + ans[biggest_a+1:]
        
        return ''
                