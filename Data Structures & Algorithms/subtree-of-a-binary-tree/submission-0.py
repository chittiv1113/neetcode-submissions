# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True 
        if not root:
            return False 

        def sameTree(a, b):
            if not a and not b:
                return True 
            if not a or not b or a.val != b.val:
                return False 
            left = sameTree(a.left, b.left)
            right = sameTree(a.right, b.right)
            return left and right
        
        q = deque([root])
        res = False
        while q:
            node = q.popleft()
            if node and node.val == subRoot.val:
                res = sameTree(node, subRoot)
            if res == True:
                return True
            if node.left: 
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return False
