# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = [0]
        def dfs(node, state):
            if not node:
                return 
            
            if node.val >= state:
                res[0] += 1
            state = max(state,node.val)
            dfs(node.left, state)
            dfs(node.right, state)
        dfs(root, root.val)
        return res[0]
            
            
            
