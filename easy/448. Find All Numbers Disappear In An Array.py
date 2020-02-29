class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for num in nums:
            index = abs(num) - 1
            nums[index] = -abs(nums[index])
        
        return [i + 1 for i, num in enumerate(nums) if num > 0]


    
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        set_num = set(nums)
        return_num = []
        for num in range(1, len(nums) + 1):
            if num not in set_num:
                return_num.append(num)
        
        return return_num

    
