class Solution: #mine
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        
        orders.sort(key=lambda x: [int(x[1]), x[2]])
        
        dict_ = defaultdict(list)
        
        unique_food = set()
        
        for o in orders:
            dict_[o[1]].append(o[2])
            unique_food.add(o[2])
            
        table_num = len(dict_)
        unique_food = sorted(list(unique_food))
        
        ans = [['Table'] + unique_food] + [['0']*(len(unique_food)+1) for _ in range (table_num)]
        
        for index, (key, val) in enumerate(dict_.items()):
            
            ans[index+1][0] = key #table number
            
            for indexx, food_count in enumerate(ans[index+1][1:]):
                for food in val:

                    if unique_food[indexx] == food:
                        ans[index+1][indexx+1] = str(int(ans[index+1][indexx+1]) + 1)
                        
        return ans

#Reference: 
# https://leetcode.com/problems/display-table-of-food-orders-in-a-restaurant/discuss/586566/Clean-Python-3-hashmap-O(N-%2B-TlogT-%2B-FlogF-%2B-T-*-F)
class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        
        dict_ = defaultdict(Counter)
        
        unique_food = set()
        
        for o in orders:
            dict_[o[1]][o[2]] += 1
            unique_food.add(o[2])
            
        unique_food = sorted(list(unique_food))
        
        ans = [['Table'] + unique_food]
        
        for table in sorted(dict_, key=int):
            ans.append([table] + [str(dict_[table][food]) for food in unique_food])
        
        return ans
           
                        