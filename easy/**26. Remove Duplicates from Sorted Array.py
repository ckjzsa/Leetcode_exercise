class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0: 
            return

        p1 = 0
        count = 0

        for p2 in range(len(nums)):
            if nums[p1] != nums[p2]:
                p1 += 1
                nums[p1] = nums[p2]
                count += 1

        length = len(nums) - 1
        for _ in range(length - count):
            nums.pop()
