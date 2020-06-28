# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthLargest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        num = []

        def mid(root):
            if root is None:
                return 
            mid(root.left)
            num.append(root.val)
            mid(root.right)
        
        mid(root)

        return num[-k]
