# https://www.programiz.com/dsa/binary-tree

class Node:
    def __init__(self, key) -> None:
        self.left = None
        self.right = None
        self.val = key

#     def traversePreOrder(self):
#         print(self.val, end= ' ')
#         if self.left:
#             self.left.traversePreOrder()
#         if self.right:
#             self.right.traversePreOrder()
    
#     def traverseInOrder(self):
#         if self.left:
#             self.left.traverseInOrder()
#         print(self.val, end= ' ')
#         if self.right:
#             self.right.traverseInOrder()

# ref) https://ejklike.github.io/2018/01/09/traversing-a-binary-tree-1.html
class BinarySearchTree(object):

    def __init__(self):
        self.root = None
    

    def insert(self, data):
        self.root = self._insert_value(self.root, data)
        return self.root is not None

    def _insert_value(self, node, data):
        if node is None:
            node = Node(data)
        else:
            if data <= node.data:
                node.left = self._insert_value(node.left, data)
            else:
                node.right = self._insert_value(node.right, data)
        return node

