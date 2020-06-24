# 递归法，层序遍历待完成

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = 0

        def depth(root, res):
            if root is None:
                return res
            else:
                res += 1
            
            return max(depth(root.left, res), depth(root.right, res))
        
        res = depth(root, res)
        return res
