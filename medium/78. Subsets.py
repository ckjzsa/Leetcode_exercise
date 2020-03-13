class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]

        for num in nums:
            result = result + [[num] + item for item in result]
        
        return result
