# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        value = []

        def preorder(root):
            if root is None:
                return 
            value.append(root.val)
            preorder(root.left)
            preorder(root.right)
        
        preorder(root)

        for i in range(len(value)-1):
            if root.right is None:
                temp = TreeNode(value[i+1])
                root.right = temp

            root.val = value[i]
            root.left = None
            root = root.right
