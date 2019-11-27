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
        def dis(root1, root2):
            if root1 == None and root2 == None:
                return True
            if root1 == None and root2 != None:
                return False
            if root1 != None and root2 == None:
                return False
            
            return (root1.val == root2.val) and (dis(root1.left, root2.right)) and (dis(root1.right, root2.left))
        
        return dis(root, root)
