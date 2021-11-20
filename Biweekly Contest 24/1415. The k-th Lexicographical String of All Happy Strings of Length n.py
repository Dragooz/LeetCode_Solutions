#Reference: https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/discuss/586165/Python3-Easy-Python3-BFS-%2B-Graph-Like

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        
        next_letter ={ 'a': 'bc', 'b': 'ac', 'c': 'ab'}
        
        queue = deque(['a', 'b', 'c'])
        
        while len(queue[0]) != n:
            u = queue.popleft()
            
            for v in next_letter[u[-1]]: #based on the last letter, add next letter each.
                queue.append(u+v)
                
        return queue[k-1] if len(queue) >= k else ''
            
            
            
            
        
                    