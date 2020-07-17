class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        res = 1
        if x == 0:
            return 0

        if n < 0:
            x = 1 / x
            n = -n
        
        while n:
            if n & 1:  # 奇数多乘一个x
                res *= x
            x *= x

            n >>= 1
        
        return res
