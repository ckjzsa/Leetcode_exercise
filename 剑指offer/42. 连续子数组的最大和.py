class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """      
        dp = [0] * (len(nums)+1)

        for i in range(len(nums)):
            dp[i+1] = max(0, nums[i]+dp[i])

        if max(dp) == 0:
            return max(nums)

        return max(dp)
