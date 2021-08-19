#Reference: https://leetcode.com/problems/closest-dessert-cost/discuss/1085820/Python3-top-down-dp by lenchen1112

class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        
        closest = lambda x: (abs(target-x), x) #tell the min how to pick minimum
        
        
        def dfs(i, cur_cost): #index to track which topping, cur_cost to track the cost.
            
            if i == len(toppingCosts) or cur_cost > target: #if reached non existing last topping or cost>target:
                return cur_cost
            
            temp_list = []
            for j in range(3):
                temp_list.append(dfs(i+1, cur_cost+(j*toppingCosts[i]))) #create 3 branches for next topping, (either 0, 1 or 2 topping)
                
            return min(temp_list, key=closest) #return the min for each 
        
        ans_list = [] 
        for bc in baseCosts:
            ans_list.append(dfs(0, bc))
        
        return min(ans_list, key=closest)
                
            