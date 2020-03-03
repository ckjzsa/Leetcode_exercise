# Time complexity is O(n2)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for k in range(i+1, len(nums)):
                if nums[i] + nums[k] == target:
                    return [i, k]


# O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for index, num in enumerate(nums):
            temp = target - num
            if temp in hashmap:
                return [hashmap[temp], index]
            
            hashmap[num] = index
        
        return None
