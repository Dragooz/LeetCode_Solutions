class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        
        started = False #to ensure its substring #largest always at the beginning
        ans = num
        for index, char in enumerate(num):
            if started and int(char) > change[int(char)]:
                break
            if int(char) < change[int(char)]:
                started = True
                ans = ans[:index] + str(change[int(char)]) + ans[index+1:]
                
        return ans