class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        #main idea:
        #each chalk will decrement k by chalk
        #k = k % sum(chalk)
        #walkthrough the chalk again
        
        chalk_sum = sum(chalk)
        
        k = k%chalk_sum
        
        if k == 0:
            return 0
        
        for index, c in enumerate(chalk):
            k = k - c
            
            if k <0:
                return index
        