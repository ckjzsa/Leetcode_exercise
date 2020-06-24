class Solution(object):
    def printNumbers(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        num = 0
        for i in range(n):
            num += 9 * 10 ** i 
        
        res = []
        for i in range(1, num+1):
            res.append(i)
        
        return res
