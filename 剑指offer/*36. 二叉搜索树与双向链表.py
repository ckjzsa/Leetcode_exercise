"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        def inorder(root):
            if not root:
                return 
            inorder(root.left)
            if self.pre:
                self.pre.right = root
                root.left = self.pre
            else:
                self.head = root  # 说明这个为起始点
            self.pre = root
            inorder(root.right)
        
        if not root:
            return 
        self.pre = None
        inorder(root)

        self.head.left = self.pre
        self.pre.right = self.head

        return self.head
