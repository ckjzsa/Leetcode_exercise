class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        index = []
        if len(nums) == 1:
            return 0

        nums_sort = sorted(nums)
        for i in range(len(nums)):
            if nums[i] != nums_sort[i]:
                index.append(i)
        
        if len(index) == 0:
            return 0

        minimum = min(index)
        maximum = max(index)

        return maximum - minimum + 1
