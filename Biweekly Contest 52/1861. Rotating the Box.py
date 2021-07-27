from collections import Counter

class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        #rotate the box 
        #get the col
        #split obstacles, rearrange the stone and empty space
        #return ans
        
        rotated_box = [list(i) for i in zip(*box[::-1])]
        
        n = len(rotated_box[0]) 
        ans = []
        
        print(rotated_box)
        for row in range(n):
            check_col = ''.join([i[row] for i in rotated_box])
            ob_position = [i for i, x in enumerate(check_col) if x == "*"]
            
            splitted = check_col.split('*')
            temp_ans = []
            for split in splitted:
                count = Counter(split) #reorganize
                temp_ans += ['.']*(count['.'] ) + ['#']*(count['#']) #empty> stone > obstacle
                
            #add back the obstacle
            for obi in ob_position:
                temp_ans.insert(obi, '*')
            
            ans.append(temp_ans)
            
        return list( [i for i in zip(*ans)] )
                
                
                
                
                
                        
        