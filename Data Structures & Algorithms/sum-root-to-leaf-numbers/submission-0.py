# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = []

        def dfs(node, state):
            if not node:
                return 
            state.append(node.val)
            if not node.left and not node.right:
                res.append(state[:])
           
            dfs(node.left, state)
            dfs(node.right, state)
            state.pop()
            

        dfs(root,[])
        total = 0
        for i in res:
            total += int("".join(map(str,i)))
        return total 