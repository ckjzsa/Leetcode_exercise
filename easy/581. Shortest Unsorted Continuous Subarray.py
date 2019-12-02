class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start, end = 0, 0
        id_start, id_end = 0, 0
        nums_sorted = sorted(nums)
        j = -1
        for i in range(len(nums)):
            if id_start == 0:
                if nums[i] != nums_sorted[i]:
                    start = i
                    id_start += 1
            if id_end == 0:
                if nums[j] != nums_sorted[j]:
                    end = j
                    id_end += 1

            j = j - 1

        if end == 0:
            return 0

        return len(nums) + end + 1 - start
