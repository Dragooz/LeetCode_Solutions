from heapq import *

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        #use heap. (enqueue time, processing time, index) to track tasks' index
        #heapify tasks so that it follows enqueue time
        #creating a processing_heap to track available tasks.
        #push only the time needed to process and index, heappop(tasks)[1:], into processing_heap
        
        tasks = [task + [index] for index, task in enumerate (tasks)]
        
        heapify(tasks)
        processing_heap = []
        ans = []
        
        time = tasks[0][0]
        cpu = True #idle or not
        
        while tasks: #loop till no tasks
            # print('time now:', time)
            # print('time of task:', tasks[0][0])
            while tasks and tasks[0][0] == time:
                heappush(processing_heap, heappop(tasks)[1:]) #pending tasks
                # print('stuck this loop')
            
            if cpu == False and time==release_time:
                release_time = 10**9 + 1 #reset release time
                cpu = True
            
            if cpu == True and processing_heap:
                pro_time, index = heappop(processing_heap)
                release_time = pro_time + time
                ans.append(index)
                cpu = False
            
            if tasks != []:
                time = min(release_time, tasks[0][0]) #update time

        while processing_heap: #get rid of remaining
            ans.append(heappop(processing_heap)[1])
            
        return ans
        
        
        