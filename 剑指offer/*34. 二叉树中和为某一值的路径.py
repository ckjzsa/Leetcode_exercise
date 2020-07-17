# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        res = []
        path = []
        def helper(root, target):
            if not root:
                return 
            
            target -= root.val
            path.append(root.val)

            if target == 0 and not root.left and not root.right:
                res.append(list(path))
            
            helper(root.left, target)
            helper(root.right, target)

            path.pop()
        
        helper(root, sum)

        return res

