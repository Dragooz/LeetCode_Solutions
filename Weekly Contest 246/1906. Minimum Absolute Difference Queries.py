'''
References:
https://leetcode.com/problems/minimum-absolute-difference-queries/discuss/1284212/Python-Cumulative-sums-solution-%2B-2Liner-explained by Dbabichev

'''


class Solution(object):
    def minDifference(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        
        #create index dict
        #this is to save time from querying the same array over and over again.
        max_nums = max(nums) #this is a must, as no need repeatly get the max nums from the list to save time
        index_dict = [[0]* (max_nums+1)]
        for num in nums:
            t = index_dict[-1][:] #last row, all columns
            t[num] += 1 #increment
            index_dict.append(t)
              
        #get answer
        #main idea is compare only two rows of index_dict associated with the query range
        #example: query 0 and 2 will only compare index of row 0 and row 3 (2 +1)  [3 values to compare if diff]
        #how to compare? only takes the numbers that has different index value. (so that only the unique + existed num selected to compare)
        ans = []
        
        for s, e in queries:
            
            #get a list of num to compare (already sorted)
            num_list = []
            for one, two, num in zip(index_dict[s], index_dict[e+1], range(max_nums+1)):
                if one!=two:
                    num_list.append(num)
            
            #compare
            diff = [num_list[i+1] - num_list[i] for i in range(len(num_list)-1)]
            
            try: 
                diff = min(diff)
                ans.append(diff)
            except:
                ans.append(-1)
        
        return ans