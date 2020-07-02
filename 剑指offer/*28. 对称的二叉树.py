# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True

        def helper(root1, root2):
            if root1 is None and root2 is not None:
                return False
            elif root1 is not None and root2 is None:
                return False
            elif root1 is None and root2 is None:
                return True
            
            left = helper(root1.left, root2.right)
            right = helper(root1.right, root2.left)

            return root1.val == root2.val and left and right

        return helper(root.left, root.right)

            
