# Time complexity is O(n2)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        for num in nums:
            if nums.count(num) > len(nums) / 2:
                return num
       
