class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cum_sum = 0
        maximum = nums[0]

        for i in range(len(nums)):
            if cum_sum >= 0:
                cum_sum += nums[i]
            elif cum_sum <= 0:
                cum_sum = nums[i]
            maximum = max(maximum, cum_sum)
        
        return maximum
