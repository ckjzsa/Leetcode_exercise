class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_i = 0

        for i, jump in enumerate(nums):
            if max_i >= i and i + jump >= max_i:
                max_i = i + jump

        return max_i >= len(nums) - 1
