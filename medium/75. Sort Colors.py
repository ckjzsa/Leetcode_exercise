class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2:
            return 
        
        zero = 0
        two = len(nums) - 1

        i = 0
        while i <= two:
            if nums[i] == 0:
                # 保证zero前面都是0
                nums[i], nums[zero] = nums[zero], nums[i]
                i += 1
                zero += 1
            elif nums[i] == 1:
                # zero和two之间都是1
                i += 1
            elif nums[i] == 2:
                nums[i], nums[two] = nums[two], nums[i]
                two -= 1
