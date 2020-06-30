class Solution(object):
    def findContinuousSequence(self, target):
        """
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        num = []

        for i in range(1, target):
            num.append(i)
        
        for root in range(len(num)):
            pos = root
            temp = num[root]
            while temp < target and (pos + 1) < len(num):
                pos += 1
                temp += num[pos]
            
            if temp == target:
                res.append(num[root:pos+1])
        
        return res
