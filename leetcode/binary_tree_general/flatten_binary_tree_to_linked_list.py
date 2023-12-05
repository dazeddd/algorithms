from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # dfs

        node_stack = []

        if not root :
            return
        
        currenct_node = root
        # node_stack += [currenct_node.left, currenct_node.rigth]

        # for node in node_stack:

        # if currenct_node.left:
        #     currenct_node.right = currenct_node

        # right_node = currenct_node.right


        