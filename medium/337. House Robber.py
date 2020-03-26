# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 递归法
class Solution:
    @functools.lru_cache(None)
    def rob(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        # 抢然后抢下下个
        left = 0 if root.left is None else self.rob(root.left.left) + self.rob(root.left.right)
        right = 0 if root.right is None else self.rob(root.right.left) + self.rob(root.right.right)
        rob = root.val + left + right

        # 不抢然后抢下一个
        not_rob = self.rob(root.left) + self.rob(root.right)

        return max(rob, not_rob)

# 更好的DP法

class Solution:
    def rob(self, root: TreeNode) -> int:
        def dp(root):  # 返回抢和不抢的最大值
            if not root:
                return 0, 0
            elif not root.left and not root.right:
                return root.val, 0

            left = dp(root.left)
            right = dp(root.right)

            return root.val + left[1] + right[1], \
                   max(left[0]+right[0], left[1]+right[0], left[1]+right[1], left[0]+right[1])
        
        return max(dp(root))
