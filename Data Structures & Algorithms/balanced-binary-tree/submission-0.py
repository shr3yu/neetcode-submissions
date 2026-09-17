# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def heightandcheck(root):
            if root is None:
                return [True, 0]
            
            leftsubtree = heightandcheck(root.left)
            rightsubtree = heightandcheck(root.right)

            balanced = leftsubtree[0] and rightsubtree[0] and abs(leftsubtree[1]-rightsubtree[1]) <= 1

            return [balanced, max(leftsubtree[1], rightsubtree[1])+1]
        
        return heightandcheck(root)[0]

            


        