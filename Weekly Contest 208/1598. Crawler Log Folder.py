class Solution:
    def minOperations(self, logs: List[str]) -> int:
        ans = []
        
        for log in logs:
            if log == '../':
                if ans:
                    ans.pop(-1)
            elif log == './':
                pass
            else:
                ans.append(log)
                
        print(ans)
        return len(ans)