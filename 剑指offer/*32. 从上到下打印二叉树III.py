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
        queue = []
        queue.append(root)

        if not root:
            return []
            
        while queue:
            temp = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                if len(res) % 2:
                    temp.insert(0, node.val)
                else:
                    temp.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            res.append(temp)

        return res
