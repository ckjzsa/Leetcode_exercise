class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 1:
            return 1
        elif len(nums) == 2:
            if nums[0] == nums[1]:
                nums.pop()
                return 1
            else:
                return 2
        else:
            p1 = 0
            for p2 in range(len(nums)):
                if nums[p1] != nums[p2]:
                    p1 += 1
                    nums[p1] = nums[p2]

            return p1 + 1
