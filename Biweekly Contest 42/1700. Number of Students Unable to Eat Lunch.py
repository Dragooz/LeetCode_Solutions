class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        ones = 0
        zeros = 0
        for s in students:
            if s==1:
                ones+=1
            else:
                zeros+=1
        
        ans = len(students)
        for s in sandwiches:
            if s == 1:
                ones -= 1
            else:
                zeros -=1
            
            if ones == -1 or zeros == -1:
                return ans
            
            ans-=1
        
        return 0