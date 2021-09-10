class Solution:
    def reformatNumber(self, number: str) -> str:
        number = number.replace(' ', '').replace('-', '')
        
        ans = ''
        
        i =0
        while i<len(number):
            if len(number) - i <= 4:
                if len(number) - i == 4:
                    ans += number[i:i+2] + '-' + number[i+2:]
                else:
                    ans += number[i:]
                break
            else:
                ans += number[i:i+3] + '-'
                i +=3

        return ans