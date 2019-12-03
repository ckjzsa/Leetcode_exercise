class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        max_ = [0 for _ in range(len(nums))]
        max_[0] = nums[0]
        max_[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            max_[i] = max(max_[i - 2] + nums[i], max_[i - 1])

        return max_[-1]
