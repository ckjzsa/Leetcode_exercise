# Time complexity is O(n2)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        for num in nums:
            if nums.count(num) > len(nums) / 2:
                return num
       
# correct answer, O(nlogn)
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        count = 1
        if len(nums) == 1:
            return nums[0]
        else:
            for i in range(1, len(nums)):
                if nums[i - 1] == nums[i]:
                    count += 1

                if count > len(nums) / 2:
                    return nums[i]
            
    
# better answer, O(n)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        set_ = set(nums)
        dict_ = {}
        for i in set_:
            dict_[str(i)] = 0
        
        for i in nums:
            dict_[str(i)] += 1
        
            if dict_[str(i)] > len(nums) / 2:
                return i


    
