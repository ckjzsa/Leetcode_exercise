class Solution(object):
    def twoSum(self, n):
        """
        :type n: int
        :rtype: List[float]
        """
        dp = [[0 for i in range(6 * n + 1)] for j in range(n + 1)]
        for i in range(1, 7):
            dp[1][i] = 1

        for i in range(2, n+1):
            for j in range(i, i*6+1):
                for k in range(1, 7):
                    if j >= k:
                        dp[i][j] += dp[i-1][j-k]
        
        res = []
        sum_ = 6 ** n
        for i in range(n, n*6+1):
            res.append(dp[n][i] * 1.0 / sum_)

        return res

