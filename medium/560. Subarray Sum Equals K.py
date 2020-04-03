class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        hash = {0:1}
        sum = 0
        count = 0

        for i in range(len(nums)):
            sum += nums[i]

            if (sum-k) in hash:
                count += hash[sum-k]

            if sum in hash:
                hash[sum] += 1
            elif sum not in hash:
                hash[sum] = 1
        
        return count
