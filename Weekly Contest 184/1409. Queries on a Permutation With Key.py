class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        
        arr = list(range(1, m+1))
        
        ans = []
        
        for q in queries:
            q_pos = arr.index(q)
            ans.append(q_pos)
            
            arr = [arr[q_pos]] + arr[:q_pos] + arr[q_pos+1:]
            
        return ans