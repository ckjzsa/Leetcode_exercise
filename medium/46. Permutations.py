class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first = 0):
            if first == n:
                res.append(nums[:])
                return res

            for i in range(first, n):
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first + 1)
                nums[i], nums[first] = nums[first], nums[i]


        res = []
        n = len(nums)
        backtrack()

        return res
