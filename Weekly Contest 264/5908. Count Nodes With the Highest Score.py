#Reference: https://leetcode.com/problems/count-nodes-with-the-highest-score/discuss/1537511/Python3-post-order-dfs

class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        tree = defaultdict(list)
        
        for i, x in enumerate(parents):
            if x>=0:
                tree[x].append(i)
                
        freq = defaultdict(int)
        
        def fn(x):
            left = right = 0
            
            if tree[x]:
                left = fn(tree[x][0])
                # print(left)
            if len(tree[x]) > 1:
                right = fn(tree[x][1])
                # print(right)
                
            score = (right or 1) * (left or 1) * ((len(parents) - 1 - left - right) or 1)
            
            freq[score] += 1
            return 1 + left + right
        
        fn(0)
        # print(freq)
        
        return freq[max(freq)]