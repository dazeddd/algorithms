from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        # each binary tree
        # p,q both None
        if not p and not q:
            return True

        # p or q is None
        if not q or not p:
            return False

        # compare by node value
        if p.val != q.val:
            return False
        # else:
        #     return True

        return self.isSameTree(p.right, q.right) and \
            self.isSameTree(p.left, q.left)
