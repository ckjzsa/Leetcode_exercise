# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):


    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maximum = 0
        if root is None:
            return 0
        self.deep(root)

        return self.maximum

    def deep(self, root):
        if root is None:
            return 0
        left = self.deep(root.left)
        right = self.deep(root.right)

        self.maximum = max(self.maximum, left + right)

        return max(left, right) + 1 
