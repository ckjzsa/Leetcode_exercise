class Solution(object):
    def isStraight(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums_dict = {}
        for i in set(nums):
            nums_dict[i] = 0
        
        minimum = max(nums)

        for i in nums:
            if i == 0:
                continue
            nums_dict[i] += 1
            if i <= minimum:
                minimum = i
            if nums_dict[i] > 1:
                return False
        
        return max(nums) - minimum <= 4
        
