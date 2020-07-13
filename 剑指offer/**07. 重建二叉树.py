# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        self.dic, self.po = {}, preorder
        for i in range(len(inorder)):
            self.dic[inorder[i]] = i

        return self.recur(0, 0, len(inorder) - 1) # 根(先序)、左子树(中序)、右子树(中序)

    def recur(self, pre_root, in_left, in_right):
        if in_left > in_right: 
            return # 终止条件：中序遍历为空
        root = TreeNode(self.po[pre_root]) # 建立当前子树的根节点
        i = self.dic[self.po[pre_root]]    # 搜索根节点在中序遍历中的索引，从而可对根节点、左子树、右子树完成划分。
        root.left = self.recur(pre_root + 1, in_left, i - 1) # 开启左子树的下层递归
        root.right = self.recur(pre_root + i - in_left + 1, i + 1, in_right) # 开启右子树的下层递归

        return root # 返回根节点，作为上层递归的左（右）子节点
