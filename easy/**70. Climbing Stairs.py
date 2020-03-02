# 复杂度太高，递归

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        s1 = 1
        s2 = 2

        def climb(leftsteps):
            
            if leftsteps == 1:
                return 1
            if leftsteps == 2:
                return 2
            if leftsteps == 3:
                return 3

            return climb(leftsteps - s1) + climb(leftsteps - s2)
        
        return climb(n)
        
 # 动态规划
 
 class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n + 1)
        dp[0] = 0
        if n == 1:
            return 1
        if n == 2:
            return 2

        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]
