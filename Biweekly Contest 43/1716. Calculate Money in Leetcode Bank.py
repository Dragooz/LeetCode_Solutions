class Solution:
    def totalMoney(self, n: int) -> int:
        
        first_week_sum = (7/2)*(1+7)
        
        total_week = n//7
        total_day = n%7
        
        return int(sum(i*7 + first_week_sum for i in range(total_week)) + total_week*total_day + sum(i for i in range(1, total_day+1)))