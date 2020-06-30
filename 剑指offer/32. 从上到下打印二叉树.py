# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        layer = 0

        def helper(root, layer):
            if root is None:
                return 
            if len(res) == layer:
                res.append([])
            
            res[layer].append(root.val)

            helper(root.left, layer + 1)
            helper(root.right, layer + 1)
        
        helper(root, layer)

        return res
