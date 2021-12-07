#Reference: https://leetcode.com/problems/validate-binary-tree-nodes/discuss/939381/Python%3A-clean-BFS-96-faster-TimeComplexity%3A-O(n)-Space-Complexity%3A-O(n)

class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        
        #find root
        child = set(leftChild+rightChild) #if inside here means it's a children.
        
        root = 0
        counter = 0
        for i in range(n):
            if i not in child:
                counter+=1
                if counter >1:
                    return False
                root = i
        
        #visited node
        visited = set()
        
        #bfs
        queue = deque([root])
        
        while queue:
            node = queue.popleft()
        
            if node in visited: #appears to have two arrows pointing to the same node
                return False
                
            visited.add(node) #number of nodes should match with ori n
            
            if leftChild[node] != -1: #it means this node has children
                queue.append(leftChild[node])
                
            if rightChild[node] != -1:
                queue.append(rightChild[node])
        
        return len(visited) == n
                 
            
        
        