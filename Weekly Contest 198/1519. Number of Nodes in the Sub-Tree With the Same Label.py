#Reference: https://leetcode.com/problems/number-of-nodes-in-the-sub-tree-with-the-same-label/discuss/743150/Clean-Python-3-dfs-with-counter

class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        
        tree = collections.defaultdict(list)
        
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)
            
        results = [0]*n
        
        def dfs(node, parent):
            
            counter = collections.Counter()
            for child in tree[node]:
                if child == parent:
                    continue 
                counter += dfs(child, node)
            
            counter[labels[node]] += 1
            results[node] = counter[labels[node]]
            return counter
            
        dfs(0, None)
        return results
        