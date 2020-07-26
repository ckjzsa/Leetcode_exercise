class Solution(object):
    def singleNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ret = 0
        for n in nums:
            ret ^= n
        
        h = 1
        while ret & h == 0:
            h <<= 1
        
        a = 0
        b = 0
        for n in nums:
            if n & h:  # 该位为1和为0分为两组，其他相同的数字都抵消了
                a ^= n
            else:
                b ^= n
        
        return [a, b]
