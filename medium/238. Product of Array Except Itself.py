class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1 for _ in range(len(nums))]
        k = 1
        for i in range(len(nums)):
            res[i] = res[i] * k
            k = k * nums[i]
        
        k = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] = res[i] * k
            k = k * nums[i]
        
        return res
