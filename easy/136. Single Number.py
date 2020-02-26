class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = 0
        for i in nums:
            a ^= i
        
        return a

    
    
    
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        else:
            set_ = set(nums)
            dict_ = {}
            for i in set_:
                dict_[str(i)] = 0
            
            for i in nums:
                dict_[str(i)] += 1
            
            return int(min(dict_, key=dict_.get))
