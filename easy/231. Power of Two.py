class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        elif n == 1 or n == 2:
            return True
        elif n % 2 == 1:  # 为奇数
            return False
        elif n % 2 == 0:
            return self.isPowerOfTwo(n / 2)

