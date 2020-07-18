class Solution(object):
    def cuttingRope(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n+1)
        dp[0] = 1 
        dp[1] = 1
        
        for i in range(2, n+1):
            for j in range(1, i):
                dp[i] = max(dp[i], dp[i-j]*j, (i-j)*j)
        
        return dp[n]
