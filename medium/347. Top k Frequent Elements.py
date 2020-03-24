class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res_dict = {}
        for num in set(nums):
            res_dict[num] = 0

        for num in nums:
            res_dict[num] += 1
        
        res = []
        keys = list(res_dict.keys())
        values = list(res_dict.values())
        for i in range(k):
            index = values.index(max(values))
            res.append(keys[index])
            keys.pop(index)
            values.pop(index)
        
        return res
