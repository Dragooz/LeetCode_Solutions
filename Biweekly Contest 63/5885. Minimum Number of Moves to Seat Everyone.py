class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        
        seats.sort()
        students.sort()
        
        ans = 0
        for s1, s2 in zip(seats, students):
            ans += abs(s2 - s1)
            
        return ans