class Solution:
    def memLeak(self, memory1: int, memory2: int) -> List[int]:
        
        #main idea:
        #which memory high, sub which
        
        
        time = 1
        while True:
            
            if memory1 >= memory2:
                if memory1 - time < 0:
                    return [time, memory1, memory2]
                memory1 -= time
            else:
                if memory2 - time <0:
                    return [time, memory1, memory2]
                memory2 -= time
                
            time+=1