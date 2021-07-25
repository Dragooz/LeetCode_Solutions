#Reference:
#https://leetcode.com/problems/maximum-compatibility-score-sum/discuss/1360805/Backtracking-with-STL-or-10-lines-of-code-or-C%2B%2B by av1shek

import itertools

class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        #main idea:
        #make a score list of each students to each mentors
        #get the permutation list to brute force
        #for example, first loop, get the first student to first mentor, second to second, third to third, and record the sum
        #Second loop, get the first to second, second to first, and all possible combination, record the sum.
        #return the max.
        
        student_score = [] # student -> mentor1, mentor2 ... 
        
        for student in students:
            temp_score = []
            for mentor in mentors:
                score = sum([a==b for a,b in zip(student, mentor)])
                temp_score.append(score)
                
            student_score.append(temp_score)
        
        index_list = [i for i in range(len(student_score))]
        
        permutation_list = list(itertools.permutations(index_list))
        
        ans = 0
        for  p in permutation_list: #try all combination
            temp = 0
            for index, p_val in enumerate(p):
                temp += student_score[index][p_val]
                
            if ans < temp:
                ans = temp
                
        return ans