# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    diameter = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        self._height(root)

        return self.diameter

    def _height(self, node:Optional[TreeNode]) -> int:
        if node is None:
            return 0
        leftheight = self._height(node.left) 
        rightheight = self._height(node.right)

        self.diameter = max(self.diameter, leftheight + rightheight)

        return max(leftheight, rightheight) + 1 



        