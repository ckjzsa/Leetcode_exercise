class Solution(object):
    def minNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        def qSort(nums, low, high):
             if low < high:
                p = Partition(nums, low, high)
                qSort(nums, low, p-1)
                qSort(nums, p+1, high)

        def Partition(nums, low, high):
            p = nums[low]
            while low < high:
                while low < high and nums[high] + p > p + nums[high]:
                    high -= 1
                if low < high:
                    nums[low] = nums[high]
                    low += 1
                
                while low < high and nums[low] + p < p + nums[low]:
                    low += 1
                if low < high:
                    nums[high] = nums[low]
                    high -= 1
            nums[low] = p
            return low
        
        str_nums = [str(num) for num in nums]
        qSort(str_nums, 0, len(str_nums)-1)
        
        return "".join(str_nums)

