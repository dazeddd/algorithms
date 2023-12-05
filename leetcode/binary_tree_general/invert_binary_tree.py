from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# https://www.algodale.com/problems/invert-binary-tree/
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        # using recursion
        if not root:
            return

        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

        # using stack
        # stack = [root]
        # while stack:
        #     node = stack.pop()
        #     if not node:
        #         continue

        #     node.left, node.right = node.right, node.left
        #     stack += [node.left, node.right]

        # return root
