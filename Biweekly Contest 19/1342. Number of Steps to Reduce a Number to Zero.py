class Solution:
    def numberOfSteps(self, num: int) -> int:
        ans = 0
        while num!=0:
            print(num)
            if num%2 == 0:
                num = num//2
                ans+=1
            elif num==1:
                ans+=1 
                return ans
            else:
                num = num//2
                ans+=2
                
        return ans