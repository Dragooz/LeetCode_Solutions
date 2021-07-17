'''
First try here, time limit exceed. 
'''

class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        
        #main idea:
        #A dictionary, with weights as key, tracking index and time.
        #Iterate through the tasks, and assign to each server accordingly. 
        #if the time != 0, then skip it. (the server busying)
        #priority given to server with smallest weights
        
        sl, tl = len(servers), len(tasks)
        
        server_time = {}
        
        for index, server in enumerate(servers):
            try:
                if server_time[server]:#exist
                    pass
                server_time[server].append((index, 0))
            except:
                server_time[server] = [(index, 0)] # weights: (index, time)
                
        server_time = dict(sorted(server_time.items()))
        # print(server_time)
        
        ans = [] 
        queue = []
        to_decrement = []
        
        while tasks != [] or queue !=[]: #make this infinite until tasks and queue are done        
            # print(server_time)
            
            temp_to_decrement = to_decrement.copy()
            if tasks != []:
                queue.append(tasks.pop(0))
                
            for w, ti in temp_to_decrement:
                server_time[w][ti] = (server_time[w][ti][0], server_time[w][ti][1]-1)
                if server_time[w][ti][1] == 0:
                    to_decrement.remove((w, ti))

            for weights, values in server_time.items():

                for tuple_index, (index, time) in enumerate(values):

                    if time == 0 and queue!=[]: #assign task
                        server_time[weights][tuple_index] = (index, queue.pop(0)) #index, time
                        to_decrement.append((weights, tuple_index)) #track which need to decrement time by 1 each loop
                        ans.append(index)

                    if queue == []: #exit here if queue is emptied
                        break

                if queue == []: #exit here if queue is emptied
                    break

        return ans

'''
Second try, get inspiration to use heap from discussion.
Reference:https://leetcode.com/problems/process-tasks-using-servers/discuss/1239767/Python-3-Simulation-Heap-Solution by shitholer
'''

import heapq

class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        
        #main idea:
        #use heap
        
        free = [[w, index] for index, w in enumerate(servers)] #weight, index
        busy = [] #server in busy, cannot use. format: time, weight, index
        
        heapq.heapify(free) #heapify
        
        ans= []
        for t, task in enumerate(tasks):
            
            while busy and busy[0][0] == t: #pop out busy to free when it is the time when the server is done
                _, weight, index = heapq.heappop(busy)
                heapq.heappush(free, [weight, index])
            
            if free: #still have available server to assign
                weight, index = heapq.heappop(free) #pop so that can be added to busy list
            else: #force busy to pop
                t, weight, index = heapq.heappop(busy) #t updated here, always larger than ori t. In here, it change from busy>free>busy
            ans.append(index) #add answer
            heapq.heappush(busy, [t+task, weight, index]) #t+task is to bring forward the force time.
            
        return ans
            
            
        