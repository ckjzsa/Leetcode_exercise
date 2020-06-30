class Solution(object):
    def findRepeatNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_set = set(nums)
        nums_dict = {}
        for num in nums_set:
            nums_dict[num] = 0
        
        for num in nums:
            nums_dict[num] += 1
            if nums_dict[num] > 1:
                return num
