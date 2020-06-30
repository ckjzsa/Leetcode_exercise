class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_dict = {}
        nums_set = set(nums)
        for num in nums_set:
            nums_dict[num] = 0
        
        for num in nums:
            nums_dict[num] += 1
        
        return max(nums_dict, key=nums_dict.get)
        
