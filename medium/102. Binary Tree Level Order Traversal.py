# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []

        if root is None:
            return res
        
        def help(root, level):
            if len(res) == level:
                res.append([])
            
            res[level].append(root.val)

            if root.left:
                help(root.left, level+1)
            if root.right:
                help(root.right, level+1)
        
        help(root, 0)

        return res
            
