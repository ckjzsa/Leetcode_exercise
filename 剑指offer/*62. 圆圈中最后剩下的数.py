class Solution(object):
    def lastRemaining(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        a = [i for i in range(n)]
        i = 0

        while len(a) > 1:
            i = (i + m - 1) % len(a)
            print(i)
            a.pop(i)
        
        return a[0]
